#!/usr/bin/env python3

# Copyright (c) 2024, APT Group, Department of Computer Science,
# The University of Manchester.

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

# http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import requests
import os
import sys
import subprocess
import argparse
import wget
import docker
from tabulate import tabulate
from . import config
from shlex import split as shlexSplit

# Access the 'options' dictionary from the config module
repos = config.repo_options
models = config.model_options
default_tokenizer_url = config.default_tokenizer
images_url = config.image_repo

if config.user_defined_resources_path:
    default_resources_path = config.user_defined_resources_path
else:
    default_resources_path = os.path.join(os.path.expanduser('~'),"LlamaDeckResources")

def create_table_data(config,constrains=None):
    table_data = [list(config[0].keys())]
    row = 1
    for c_row in config:
        if constrains:
            for k,i in constrains.items():
                if c_row[k].lower() == i:
                    table_data.append([row]+list(c_row.values()))
                    row += 1
        else:
            table_data.append([row]+list(c_row.values()))
            row += 1

    return table_data

def show_table(table_data):

    table = tabulate(table_data[1:],headers=table_data[0],tablefmt="pipe")

    print("\n" + "-" * 121 + "\n")
    print(table)
    print("\n" + "-" * 121 + "\n")

def run_sh(command):
    """Run a shell command.

    Args:
        command (str or list): The command to be executed. Can be a string or a list of strings.
    """

    run_command = ""
    if type(command) is list:
        for c in command:
            run_command += (c + " ")
    else:
        run_command = command

    process = subprocess.Popen(run_command, 
                               stdout=sys.stdout, 
                               stderr=sys.stdout, 
                               shell=True)
    
    process.wait()

def clone_repository(url, destination):
    """Clone a Git repository.

    Args:
        url (str): URL of the Git repository.
        destination (str): Destination directory for cloning.
    """
    try:
        subprocess.run(["git", "clone", url, destination], check=True)
        print(f"Repository cloned successfully to {destination}")
    except subprocess.CalledProcessError as e:
        print(f"Error cloning repository: {e}")

def fetch_remote_image_info():
    """Fetch image information from bufan0222/ll_implements.

    Returns:
        list: A list of dictionaries containing image information.
    """
    
    response = requests.get(images_url)
    data = response.json()  

    images = []

    for img_data in data["results"]:
        repo_name = img_data["name"].split("_")[0]
        author = img_data["name"].split("_")[1]
        
        row = {
            "Tag": img_data["name"],
            "Language":get_img_language(repo_name),
            "Size": str(img_data["full_size"]/1024//1024)+" MB",
            "Author":"@"+author,
            "Repository": "https://github.com/"+author+"/"+repo_name,

               }
        images.append(row)

    return images


def choose_options(max_option_num):
    """Prompt the user to choose several options.

    Args:
        max_option_num (int) :max valid option number.
    Returns:
        list or None: The selected options in a list or None if input is 0.
    """

    while True:
        try:
            chosen = input("Choose option from row 1 to "+str(max_option_num - 1)+
                           "\n(eg '1,2,3,4-10', input '0' to go back):")

            if chosen == '0':
                return None
                
            chosen = chosen.strip().split(",")
            res = []

            for c in chosen:

                if '-' in c:
                    startIdx = int(c.strip().split("-")[0])
                    endIdx = int(c.strip().split("-")[1])

                    if startIdx > endIdx:
                        raise ValueError
                    
                    for i in range(startIdx,endIdx+1):
                        chosen.append(str(i))
                    continue

                idx = int(c)
                if idx > 0 and idx < max_option_num:
                    res.append(idx)
                else:
                    raise ValueError
                
            return res
        except Exception:
            print("Invalid input: ", c)


def list_repos(language = None):
    """List repositories implemented in a given language.

    Args:
        language (str): The programming language to list repositories for.
    """

    if language:
        constrains = {"language":language.lower()}
        repo_table_data = create_table_data(repos,constrains)
    else:
        repo_table_data = create_table_data(repos)

    show_table(repo_table_data)

def list_models(model_name = None):
    """List available models to install.

    Args:
        model_name (str): The name of the model to list.
    """
    

    if model_name:
        constrains = {"Model":model_name.lower()}
        model_table_data = create_table_data(models,constrains)
    else:
        model_table_data = create_table_data(models)
        
    show_table(model_table_data)

def list_images(image_tag = None,language = None):
    """List available images.

    Args:
        image_tag (str): The tag of the image to list.
    """
    images = fetch_remote_image_info()

    constrains = {}
    if image_tag != None:
        constrains["Tag"] = image_tag.lower()
    if language != None:
        constrains["Language"] = language.lower()
    
    if len(constrains) != 0:
        images_table_data = create_table_data(images,constrains)
    else:
        images_table_data = create_table_data(images)
        
    show_table(images_table_data)

def install_repos(default_resources_path,language = None):
    """Install repositories for a given language.

    Args:
        path (str): The path where repositories should be installed.
        language (str): The programming language to list repositories for.
    """

    resources_path = (
        input(f"Enter the destination directory \n(press enter to using default: {default_resources_path}): "
            ).strip()
            or default_resources_path
        )
    
    if language:
        constrains = {"language":language.lower()}
        repo_table_data = create_table_data(repos,constrains)
    else:
        repo_table_data = create_table_data(repos)
    
    show_table(repo_table_data)

    if len(repo_table_data) == 1:
        print("No repository implemented in:",language)
        return

    all_selected_idx = choose_options(len(repo_table_data))
    if not all_selected_idx:
        print("Exit repo install.")
        return

    for idx in all_selected_idx:
        selected_repo = repo_table_data[idx]

        lang, name, url, author = selected_repo[1], selected_repo[2], selected_repo[3], selected_repo[4]

        destination = os.path.join(
            resources_path, "llamaRepos", lang, author, name
        )

        print("==>installing repo from row",str(idx))
        print("destination:",destination)

        try:
            """check if repo is exist"""
            os.makedirs(destination, exist_ok=False)
            clone_repository(url, destination)
            print("Finished. \n")
        except OSError as e:
            if e.errno == 17:
                print(destination,"already exist.\n")
            else:
                print(e)

    print("All selected repositories installed.")
    

def install_models(default_resources_path,model_name=None):
    """Install available models.

    Args:
        path (str): The path where models should be installed.
        model_name (str): The name of the model to install.
    """

    resources_path = (
        input(f"Enter the destination directory \n(press enter to using default: {default_resources_path}): "
            ).strip()
            or default_resources_path
        )
    
    destination = os.path.join(resources_path,"llamaModels")
    if not os.path.exists(destination):
        os.makedirs(destination)

    if model_name:
        constrains = {"Model":model_name.lower()}
        model_table_data = create_table_data(models,constrains)
    else:
        model_table_data = create_table_data(models)

    show_table(model_table_data)

    if len(model_table_data) == 1:
        print("No model named:",model_name)
        return

    all_selected_idx = choose_options(len(model_table_data))
    if not all_selected_idx:
        print("Exit model install.")
        return

    meta_model_needed = False

    for idx in all_selected_idx:
        selected_model = model_table_data[idx]

        model_name,url = selected_model[1],selected_model[2]

        if model_name == "Meta-Llama":
            meta_model_needed = True
            continue

        print("==>installing model from row",str(idx))
        print("destination:",os.path.join(destination,model_name+".bin"))

        
        """check if model is exist"""
        if not os.path.exists(os.path.join(destination,model_name+".bin")):
            download_and_configure_model(model_name,
                                         url,
                                         destination,
                                         )

        else:
            print(os.path.join(destination,model_name+".bin"),"already exist.\n")

    if meta_model_needed:
        install_meta_llama()

    print("All selected models installed.")

    check_and_install_tokenizer(resources_path)

def check_and_install_tokenizer(resources_path):
    """Ask user to download default tokenizer if no tokenizer exists.

    Args:
        default_resources_path (str): specified resources path
    """
    default_tokenizer_path = os.path.join(resources_path,"llamaTokenizers")

    if not os.path.exists(default_tokenizer_path):
        os.mkdir(default_tokenizer_path)

    if not os.path.exists(os.path.join(default_tokenizer_path,"tokenizer.bin")):
        print("\nNo tokenizer is detected in the default resources directory.")
        choice = input("Do you want to install the default tokenizer? [y to confirm]")
        if choice == 'y' or choice == "Y":
            download_and_configure_model("tokenizer",
                                         default_tokenizer_url,
                                         default_tokenizer_path,
                                         )

def install_images(image_tag = None,language = None):
    """Install images.

    Args:
        image_tag (str): The tag of the image to install.
    """

    images = fetch_remote_image_info()
    img_repo = "bufan0222/ll_implements"
    client = docker.from_env()

    constrains = {}
    if image_tag != None:
        constrains["Tag"] = image_tag.lower()
    if language != None:
        constrains["Language"] = language.lower()
    
    if len(constrains) != 0:
        images_table_data = create_table_data(images,constrains)
    else:
        images_table_data = create_table_data(images)
        
    show_table(images_table_data)

    if len(images_table_data) == 1:
        print("Image tag not found:",image_tag)
        return

    all_selected_idx = choose_options(len(images_table_data))
    if not all_selected_idx:
        print("Exit image install.")
        return
    
    for idx in all_selected_idx:
        selected_row = images_table_data[idx]

        selected_tag= img_repo+":"+selected_row[1]

        print("\n==>installing image from row",str(idx))

        local_images = client.images.list()
        img_exist = False
        for img in local_images:
            if selected_tag in img.tags:
                img_exist = True
                break

        if img_exist:
            print("Image",selected_row[1],"already exist.\n")
        else:
            run_sh("docker pull "+selected_tag)
                

    print("\n\nAll selected images installed.")



def download_and_configure_model(model_name, model_url, destination):
    """Download and configure a llama model.

    Args:
        model_name (str): Name of the llama model.
        model_url (str): URL of the llama model.
        destination_directory (str): Destination directory for the llama model.
    """

    try:
        # Download the model using wget
        wget.download(model_url, out=destination)
        print(f"\n{model_name} model downloaded successfully to {destination} \n")

        # Add logic to configure the model if needed

    except Exception as e:
        print(f"Error downloading {model_name} model: {e}")

def install_meta_llama():
    print("==> installing Meta-Llama")
    wget.download("https://raw.githubusercontent.com/meta-llama/llama/main/download.sh",out = ".")
    file_path = os.getcwd()+"/download.sh"

    print("\n\n\nMeta LLama is License protected.")
    print("Please first visit: https://llama.meta.com/llama-downloads/ to accept license and get access URL first.")
    print(f"Then follow instructions below. \n\n\n (Root privileges needed to run the download script provided by the meta team, or you can stop this process and run it by yourself: {file_path})")
    print()
    
    subprocess.run("sudo chmod 777 ./download.sh",shell=True)
    subprocess.run("./download.sh",shell=True)

    os.remove("download.sh")

    print("\n")


def is_img_supported(tag):
    """Check if an image supports this tool.

    Args:
        tag (str): The tag of the image.
    """

    client = docker.from_env()

    try:
        container = client.containers.run(tag, 
                                        command="sh -c 'test -f cli_run.py && echo llama-deck supported. || echo not supported.'", 
                                            remove=True, stdout=True)
        output = container.decode('utf-8').strip()
            
        return "llama-deck supported." in output
    
    except Exception:
        return False

def get_img_language(repo_name):
    for repo in repos:
        if repo["name"] == repo_name:
            return repo["language"]
    return "Unknown"

def select_img_to_run():
    client = docker.from_env()
    local_img = client.images.list()

    local_img_data = []

    total_img = len(local_img)
    num = 0
    for image in local_img:
        num += 1
        print(f"Finding supported images...[{num}/{total_img}]",end="\r")
        try:
            repo,tag = image.tags[0].split(":")

        except Exception:
            continue

        if is_img_supported(image.tags[0]):
            try:
                repo_name = tag.split("_")[0]
                author = tag.split("_")[1]
                repo_url = "https://github.com/"+author+"/"+repo_name
            except Exception:
                repo_url = "Unknown"
            local_img_data.append({"Installed images":f"{repo}:{tag}",
                                   "Language":get_img_language(repo_name),
                                   "Based repository":repo_url})

    if len(local_img_data) == 0:
        print("Please install images before run.")
        return None
    
    print("\n==>Select images to run:")
    local_img_table = create_table_data(local_img_data)
    show_table(local_img_table)

    all_selected_idx = choose_options(len(local_img_table))
    if not all_selected_idx:
        return None
        
    selected_img = []
    print("\n==>Selected Image:")
    for idx in all_selected_idx:
        row = local_img_table[idx]
        selected_tag = row[1]
        selected_img.append(selected_tag)
        print(selected_tag)
    
    return selected_img

def select_model_to_run():
    model_path = os.path.join(default_resources_path,"llamaModels")

    print(f"\nYou can simply choose installed model from default path: {model_path}")
    print("or specify the path to your own model.")
    c = input("Do you want to specify the model path? ['y' to confirm] ")
    if c == 'y' or c == "Y":
        model_path = input("Model Path (absolute path needed):")
        return model_path

    no_model = False
    local_models = []
    try:
        local_models = os.listdir(model_path)
    except FileNotFoundError:
        no_model = True
    
    if len(local_models) == 0:
        no_model = True
    
    if no_model:
        print("\nNo model found in:",os.path.abspath(model_path))
        print("Please install model into default path, or input your own model path.")
        return None

    print("Select an installed model to run:")

    local_model_data = []
    for model in local_models:
        dest = os.path.abspath(os.path.join(model_path,model))
        size = str(os.path.getsize(dest)/1024//1024) + " MB"
        local_model_data.append({"Model":model,"Size":size,"From":dest})
    local_model_table = create_table_data(local_model_data)
    show_table(local_model_table)

    while True:
        all_selected_idx = choose_options(len(local_model_table))
        if not all_selected_idx:
            return None
        
        if len(all_selected_idx) == 1:
            idx = all_selected_idx[0]
            selected_model_dest = local_model_table[idx][3]
            print("\n==> Selected Model:")
            print(selected_model_dest)
            return selected_model_dest
        else:
            print("Only one model can be selected at a time!\n")

def ask_run_flags(parser):
    print("\n==> Set runnning parameters (Some implementations may not support all of them.)")
    while True:

        help_str = '''
            Options:
            -t <float>  temperature in [0,inf], default 1.0
            -p <float>  p value in top-p (nucleus) sampling in [0,1] default 0.9
            -s <int>    random seed, default time(NULL)
            -n <int>    number of steps to run for, default 256. 0 = max_seq_len
            -i <string> input prompt
            -z <string> optional path to custom tokenizer
            -m <string> mode: generate|chat, default: generate
            -y <string> (optional) system prompt in chat mode

            Example: -n 256 -i "Once upon a time"

        '''

        print(help_str)

        flag_str = input("Input parameters (leave blank to using default):\n")

        try:
            namespace = parser.parse_args(shlexSplit(flag_str))
            return build_run_flags(namespace)

        except argparse.ArgumentError as e:
            print("Unknown argument.")
            continue
        except SystemExit:
            continue

            
def build_run_flags(namespace):

    flag_dict = {
        "temperature": "-t",
        "p_value": "-p",
        "seed": "-s",
        "steps": "-n",
        "input_prompt": "-i",
        "tokenizer_path": "-z",
        "mode": "-m",
        "system_prompt": "-y"
    }

    flags = ""
    print("\n==> Selected run arguments:")
    for k,v in vars(namespace).items():
        if v and k != "action":
            print(f"{k}: {v}")

            if "prompt" in k:
                v = f"'{v}'"
            if k in flag_dict:
                flags += (f"{flag_dict[k]} {v} ")

    return flags


def run_images(args,run_flag_parser):
    """Run images with specified arguments.

    Args:
        args: The arguments for running images.
        parser: The parser to handle arguments.
    """
    

    if args.image_tag is None:
        img_to_run = select_img_to_run()
    else:
        img_to_run = [args.image_tag]
    
    if img_to_run == None:
        print("Exit run images.")
        return
    
    if args.model_path is None:
        model_path = select_model_to_run()
    else:
        model_path = args.model_path
    
    if model_path == None:
        print("Exit run images.")
        return

    run_flags = ""
    for k,v in vars(args).items():
        if v and k != "action":
            run_flags = build_run_flags(args)
            break
    
    if run_flags == "":
        run_flags = ask_run_flags(run_flag_parser)
    
    for tag in img_to_run:
        inside_command = "python3 cli_run.py run /models/model.bin " + run_flags
        run_img_command = f'''docker run -it --rm -v {model_path}:/models/model.bin {tag} /bin/sh -c "{inside_command}"'''
        
        print(f"\n\nRunning {tag}...")
        print(f"\n##################stdout from {tag} ####################")
        run_sh(run_img_command)
        print("#####################################################################\n")
    
    print("All images finished.")


def main():
    """Main function to handle Llama Deck operations."""

    parser = argparse.ArgumentParser(
        description="Llama Deck: Manage and run multi llama implementations.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,  # Show default values in the help menu
    )
    subparsers = parser.add_subparsers(dest="action", help="Action to perform")

    list_repo_parser = subparsers.add_parser("list_repo", help="List repositories")
    list_repo_parser.add_argument(
        "--language", "-l",
        nargs="?",  # Make language optional
        default=None,
        help="Specify the language of repos to show in table",
    )

    # subparser: install_repo
    install_repo_parser = subparsers.add_parser("install_repo", help="Install repositories")
    install_repo_parser.add_argument(
        "--language", "-l",
        nargs="?",  # Make language optional
        default=None,
        help="Specify the language of repos to install",
    )

    # subparser: list_model
    list_model_parser = subparsers.add_parser("list_model", help="List models")
    list_model_parser.add_argument(
        "--model_name", "-m",
        nargs="?",  
        default=None,
        help="Specify the model name",
    )

    # subparser: install_model
    install_model_parser = subparsers.add_parser("install_model", help="Install models")
    install_model_parser.add_argument(
        "--model_name", "-m",
        nargs="?",  
        default=None,
        help="Specify the model name",
    )

    # subparser: list_img
    list_img_parser = subparsers.add_parser("list_img", help="List images")
    list_img_parser.add_argument(
        "--image_tag", "-i",
        nargs="?",  
        default=None,
        help="Specify the image tag",
    )
    list_img_parser.add_argument(
        "--language", "-l",
        nargs="?",  
        default=None,
        help="Specify the language of the repository inside image",
    )

    # subparser: install_img
    install_img_parser = subparsers.add_parser("install_img", help="Install images")
    install_img_parser.add_argument(
        "--image_tag", "-i",
        nargs="?",  
        default=None,
        help="Specify the image tag",
    )
    install_img_parser.add_argument(
        "--language", "-l",
        nargs="?",  
        default=None,
        help="Specify the language of the repository inside image",
    )

    # subparser: run_img
    run_img_parser = subparsers.add_parser("run_img", help="Run image with specified options")
    run_img_parser.add_argument(
        "image_tag",
        type=str,
        nargs="?",
        help="specify image to run",
    )
    run_img_parser.add_argument(
        "model_path",
        type=str,
        nargs="?",
        help="path to the model",
    )

    run_img_parser.add_argument(
        "-t", "--temperature",
        type=float,
        help="Temperature in [0, inf], default 1.0",
    )
    run_img_parser.add_argument(
        "-p", "--p_value",
        type=float,
        help="p value in top-p (nucleus) sampling in [0,1], default 0.9",
    )
    run_img_parser.add_argument(
        "-s", "--seed",
        type=int,
        help="Random seed, default time(NULL)",
    )
    run_img_parser.add_argument(
        "-n", "--steps",
        type=int,
        help="Number of steps to run for, default 256. 0 = max_seq_len",
    )
    run_img_parser.add_argument(
        "-i", "--input_prompt",
        type=str,
        help="Input prompt",
    )
    run_img_parser.add_argument(
        "-z", "--tokenizer_path",
        type=str,
        help="Optional path to custom tokenizer",
    )
    run_img_parser.add_argument(
        "-m", "--mode",
        type=str,
        choices=["generate", "chat"],
        help="Mode: generate|chat, default: generate",
    )
    run_img_parser.add_argument(
        "-y", "--system_prompt",
        type=str,
        help="(optional) system prompt in chat mode",
    )

    args = parser.parse_args()

    if args.action == "list_repo":
        list_repos(args.language)

    elif args.action == "install_repo":
        install_repos(default_resources_path,args.language)

    elif args.action == "list_model":
        list_models(args.model_name)

    elif args.action == "install_model":
        install_models(default_resources_path,args.model_name)

    elif args.action == "list_img":
        list_images(args.image_tag,args.language)

    elif args.action == "install_img":
        install_images(args.image_tag,args.language)

    elif args.action == "run_img":
        run_images(args,run_img_parser)

    else:
        parser.print_help()


if __name__ == "__main__":
    main()

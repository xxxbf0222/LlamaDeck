#!/usr/bin/env python3

import requests
import os
import subprocess
import argparse
import wget
import docker
from tabulate import tabulate
import config

# Access the 'options' dictionary from the config module
repos = config.repo_options
models = config.model_options
images_url = 'https://registry.hub.docker.com/v2/repositories/bufan0222/ll_implements/tags'

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
    
    response = requests.get(images_url)
    data = response.json()  

    images = []

    for img_data in data["results"]:
        repo_name = img_data["name"].split("_")[0]
        author = img_data["name"].split("_")[1]
        
        row = {
            "Tag": img_data["name"],
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
        list or None: The selected options into list or None.
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

    if language:
        constrains = {"language":language.lower()}
        repo_table_data = create_table_data(repos,constrains)
    else:
        repo_table_data = create_table_data(repos)

    show_table(repo_table_data)

def list_models(model_name = None):

    if model_name:
        constrains = {"Model":model_name.lower()}
        model_table_data = create_table_data(models,constrains)
    else:
        model_table_data = create_table_data(models)
        
    show_table(model_table_data)

def list_images(image_tag = None):
    images = fetch_remote_image_info()

    if image_tag:
        constrains = {"Tag":image_tag.lower()}
        images_table_data = create_table_data(images,constrains)
    else:
        images_table_data = create_table_data(images)
        
    show_table(images_table_data)

def install_repos(default_resources_path,language = None):
    """Perform interactive actions for choosing and cloning llama options.

    Args:
        default_llama_shepherd_path (str): Default path for llama shepherd.
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
            resources_path, "repos", lang, author, name
        )

        print("==>installing repo from row",str(idx))
        print("destination:",destination)

        try:
            """check if repo is exist"""
            os.makedirs(destination, exist_ok=False)
            clone_repository(url, destination)
            print("Finished. \n")
        except OSError:
            print(destination,"already exist.\n")

    print("All selected repositories installed.")
    

def install_models(default_resources_path,model_name=None):
    """Initialize llama models based on user input.

    Args:
        default_llama_shepherd_path (str): Default path for llama shepherd.
    """

    destination = os.path.join(default_resources_path,"models")

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

def install_images(image_tag = None):

    images = fetch_remote_image_info()
    img_repo = "bufan0222/ll_implements"
    client = client = docker.from_env()

    if image_tag:
        constrains = {"Tag":image_tag.lower()}
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
            pull_image(selected_tag)
                

    print("\n\nAll selected images installed.")


def pull_image(tag):
    client = docker.APIClient()

    print("Request image pull...")

    response = client.pull(tag, stream=True, decode=True)

    for progress in response:
        status = progress["status"]
        if status == "Downloading":
            print(status,progress['progress'],end='\r')
        else:
            print(status,end='\r')

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

    print("\n\n\nMeta LLama is License protected.")
    print("Please first visit: https://llama.meta.com/llama-downloads/ \nto accept license and get access URL.")
    print("Then follow instructions below:\n")
    
    subprocess.run("sudo chmod 777 ./download.sh",shell=True)
    subprocess.run("./download.sh",shell=True)

    os.remove("download.sh")

    print("\n")

def main():
    """Main function to handle llama shepherd CLI operations."""
    default_resources_path = os.path.join(os.getcwd(), "resources")

    parser = argparse.ArgumentParser(
        description="Llama Shepherd CLI: Manage your llama-related projects.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,  # Show default values in the help menu
    )
    parser.add_argument(
        "action",
        nargs="?",
        default="--help",  # Set default action to "--help"
        choices=["list_repo", "install_repo", "list_model", "install_model", 
                 "list_img","install_img","--help"],
        help="Action to perform",
    )

    parser.add_argument(
        "--language","-l",
        nargs="?",  # Make language optional
        default=None,
        help="Specify the language for the repository actions",
    )

    parser.add_argument(
        "--model_name","-mn",
        nargs="?",  # Make language optional
        default=None,
        help="Specify the model name for the model actions",
    )

    parser.add_argument(
        "--image_tag","-img",
        nargs="?",  # Make language optional
        default=None,
        help="Specify the image tag",
    )

    args = parser.parse_args()

    if args.action == "list_repo":
        list_repos(args.language)

    elif args.action == "list_model":
        list_models(args.model_name)

    elif args.action == "list_img":
        list_images(args.image_tag)

    elif args.action == "install_repo":
        install_repos(default_resources_path,args.language)

    elif args.action == "install_model":
        install_models(default_resources_path,args.model_name)

    elif args.action == "install_img":
        install_images(args.image_tag)

    elif args.action == "--help":
        parser.print_help()


if __name__ == "__main__":
    main()

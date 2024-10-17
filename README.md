# Llama Deck

**Llama Deck** is a command-line tool for quickly managing and experimenting with multiple versions of llama inference implementations. It can help you quickly filter and download [different llama implementations](#available-repositories) and [llama2-like transformer-based LLM models](#available-models). We also provide [some Docker images](#available-images) based on some implementations, which can be easily deploy and run through our tool. 

Inspired by [llama2.c project](https://github.com/karpathy/llama2.c) and forked from [llama-shepherd-cli](https://github.com/mikepapadim/llama-shepherd-cli).

## Shortcuts
[Install The Tool](#install): `pip install llama-deck`

[Manage Repositories](#explore--download-llama-repositories) : `list_repo` `install_repo` `-l <language>`

[Manage Models](#explore--download-models): `list_model` `install_model`
`-m <model_name>`

[Manage and Run Docker Images](#install--run-images) :`install_img` `run_img`

## Install 
To install the tool, simply run:
```bash
pip install llama-deck
```

## Explore & Download Llama Repositories

### List Repositories
To list all Llama Implementations, run:
```bash
llama-deck list_repo
```
You can also set `-l` to specify the language of the repository, like:
![list_repo (1)](https://github.com/user-attachments/assets/c9a987f5-efd1-4b82-a754-fe71022069bc)



### Download Repositories

You can also download those [implementation repositories](#repository-list) through our tool:
```bash
llama-deck install_repo
```
![install_repo (1)](https://github.com/user-attachments/assets/142b14b9-e274-41a4-b97a-2480edc7a1e5)


You can also set `-l` to specify a language. 
Once it runs, it supports to download multiple repositories at once, by input row numbers from the listed table. And if you don't like the default download path, you can also specify your own path to download. 

Repositories are saved and splitted by the language and the author name, you can find them in `<specified download path>/llamaRepos`.

[Back to Shortcuts](#shortcuts)



### Available Repositories

Originating from [llama2.c project](https://github.com/karpathy/llama2.c) by Andrej Karpathy. 

-------------------------------------------------------------------------------------------------------------------------

| #   | Language    | Name                     | Github                                               | Author          |
|:----|:------------|:-------------------------|:-----------------------------------------------------|:----------------|
| 1.  | Rust        | llama2.rs                | https://github.com/gaxler/llama2.rs                  | @gaxler         |
| 2.  | Rust        | llama2.rs                | https://github.com/leo-du/llama2.rs                  | @leo-du         |
| 3.  | Rust        | llama2-rs                | https://github.com/danielgrittner/llama2-rs          | @danielgrittner |
| 4.  | Rust        | llama2.rs                | https://github.com/lintian06/llama2.rs               | @lintian06      |
| 5.  | Rust        | pecca.rs                 | https://github.com/rahoua/pecca-rs                   | @rahoua         |
| 6.  | Rust        | llama2.rs                | https://github.com/flaneur2020/llama2.rs             | @flaneur2020    |
|     |             |                          |                                                      |                 |
| 7.  | Go          | go-llama2                | https://github.com/tmc/go-llama2                     | @tmc            |
| 8.  | Go          | llama2.go                | https://github.com/nikolaydubina/llama2.go           | @nikolaydubina  |
| 9.  | Go          | llama2.go                | https://github.com/haormj/llama2.go                  | @haormj         |
| 10. | Go          | llama2.go                | https://github.com/saracen/llama2.go                 | @saracen        |
|     |             |                          |                                                      |                 |
| 11. | Android     | llama2.c-android         | https://github.com/Manuel030/llama2.c-android        | @Manuel030      |
| 12. | Android     | llama2.c-android-wrapper | https://github.com/celikin/llama2.c-android-wrapper  | @celikin        |
|     |             |                          |                                                      |                 |
| 13. | C++         | llama2.cpp               | https://github.com/leloykun/llama2.cpp               | @leloykun       |
| 14. | C++         | llama2.cpp               | https://github.com/coldlarry/llama2.cpp              | @coldlarry      |
|     |             |                          |                                                      |                 |
| 15. | CUDA        | llama_cu_awq             | https://github.com/ankan-ban/llama_cu_awq            | @ankan-ban      |
|     |             |                          |                                                      |                 |
| 16. | JavaScript  | llama2.js                | https://github.com/epicure/llama2.js                 | @epicure        |
| 17. | JavaScript  | llamajs                  | https://github.com/agershun/llamajs                  | @agershun       |
| 18. | JavaScript  | llama2.ts                | https://github.com/wizzard0/llama2.ts                | @oleksandr_now  |
| 19. | JavaScript  | llama2.c-emscripten      | https://github.com/gohai/llama2.c-emscripten         | @gohai          |
|     |             |                          |                                                      |                 |
| 20. | Zig         | llama2.zig               | https://github.com/cgbur/llama2.zig                  | @cgbur          |
| 21. | Zig         | llama2.zig               | https://github.com/vodkaslime/llama2.zig             | @vodkaslime     |
| 22. | Zig         | llama2.zig               | https://github.com/clebert/llama2.zig                | @clebert        |
|     |             |                          |                                                      |                 |
| 23. | Julia       | llama2.jl                | https://github.com/juvi21/llama2.jl                  | @juvi21         |
|     |             |                          |                                                      |                 |
| 24. | Scala       | llama2.scala             | https://github.com/jrudolph/llama2.scala             | @jrudolph       |
|     |             |                          |                                                      |                 |
| 25. | Java        | llama2.java              | https://github.com/mukel/llama2.java                 | @mukel          |
| 26. | Java        | llama2.tornadovm.java    | https://github.com/mikepapadim/llama2.tornadovm.java | @mikepapadim    |
| 27. | Java        | Jlama                    | https://github.com/tjake/Jlama                       | @tjake          |
| 28. | Java        | llama2j                  | https://github.com/LastBotInc/llama2j                | @lasttero       |
|     |             |                          |                                                      |                 |
| 29. | Kotlin      | llama2.kt                | https://github.com/madroidmaq/llama2.kt              | @madroidmaq     |
|     |             |                          |                                                      |                 |
| 30. | Python      | llama2.py                | https://github.com/tairov/llama2.py                  | @tairov         |
|     |             |                          |                                                      |                 |
| 31. | C#          | llama2.cs                | https://github.com/trrahul/llama2.cs                 | @trrahul        |
|     |             |                          |                                                      |                 |
| 32. | Dart        | llama2.dart              | https://github.com/yiminghan/llama2.dart             | @yiminghan      |
|     |             |                          |                                                      |                 |
| 33. | Web         | llama2c-web              | https://github.com/dmarcos/llama2.c-web              | @dmarcos        |
|     |             |                          |                                                      |                 |
| 34. | WebAssembly | icpp-llm                 | https://github.com/icppWorld/icpp-llm                | N/A             |
|     |             |                          |                                                      |                 |
| 35. | Fortran     | llama2.f90               | https://github.com/rbitr/llama2.f90                  | N/A             |
|     |             |                          |                                                      |                 |
| 36. | Mojo        | llama2.🔥                | https://github.com/tairov/llama2.mojo                | @tairov         |
|     |             |                          |                                                      |                 |
| 37. | OCaml       | llama2.ml                | https://github.com/jackpeck/llama2.ml                | @jackpeck       |
|     |             |                          |                                                      |                 |
| 38. | Everywhere  | llama2.c                 | https://github.com/trholding/llama2.c                | @trholding      |
|     |             |                          |                                                      |                 |
| 39. | Bilingual   | llama2.c-zh              | https://github.com/chenyangMl/llama2.c-zh            | @chenyangMl     |

-------------------------------------------------------------------------------------------------------------------------
[Back to Shortcuts](#shortcuts)

## Explore & Download Models
Currently the tool only contains Tinyllamas provided in [llama2.c project](https://github.com/karpathy/llama2.c), and Meta-Llama. More model options will be extended and provided to download.

The oprations for listing and downloading models are similar to [repositories](#explore--download-llama-repositories). For list available models, run:
```bash
llama-deck list_model
```
And for download model:
```bash
llama-deck install_model
```

Similarly, `-m` is optional and can be set to specify the model name you want to show and download. 


The tool could also helps you to download the default tokenizer provided in [llama2.c](https://github.com/karpathy/llama2.c).

[Back to Shortcuts](#shortcuts)

### Available Models
More model options will be extended and provided to download.

-------------------------------------------------------------------------------------------------------------------------

|    | Model       | url                                                                     |
|---:|:------------|:------------------------------------------------------------------------|
|  1 | stories15M  | https://huggingface.co/karpathy/tinyllamas  |
|  2 | stories42M  | https://huggingface.co/karpathy/tinyllamas  |
|  3 | stories110M | https://huggingface.co/karpathy/tinyllamas |
|  4 | Meta-Llama  | https://llama.meta.com/llama-downloads/                                 |

-------------------------------------------------------------------------------------------------------------------------


**IMPORTANT!** It is lisence protected to download Meta-Llama models, which means you still needs to [apply for a download permission by Meta](https://llama.meta.com/llama-downloads). But once you received the download url from Meta's confirmation email, this tool will automatically grab and run [download.sh](https://github.com/meta-llama/llama?tab=readme-ov-file#download) provided by Meta to help you download Meta-Llama models.

[Back to Shortcuts](#shortcuts)

## Install & Run Images
In order to quickliy deploying and experimenting with multiple versions of llama inference implementations, we build an image repository consists of some dockerized popular implementations. [See our image repository](https://hub.docker.com/r/bufan0222/ll_implements/tags).

`llama-deck` can access, pull and run these dockerized implementations. When you need to run multiple implementations, or compare the performance differences between implementations, this will greatly save your effort in deploying implementations, configuring many runtime environment, and learning how to infer a certain implementation.

Before trying these functions, make sure **docker** is already installed and running on your device.

### Install DockerImages
To list images from our image repository, use:
```bash
llama-deck list_img
```
And install image:
```bash
llama-deck install_img
```

Both for `list_img` and `run_img` action, an optional flag `-i <image tag>` can be set to check if a specific tag is included. All image tags are named with format `<repository name>_<author>`. (e.g. for Karpathy's [llama2.c](https://github.com/karpathy/llama2.c), the image tag is `llama2.c_karpathy`) 

The process of installing images is mostly the same as installing repositories and models.
[Back to Shortcuts](#shortcuts)

### Run the Docker Images
There are 2 ways to run images.

#### 1 Follow the Instructions
Run:
`llama-deck run_img`

Simply call `run_img` action and let the tool find resources and helps you set all configs for model inference. After running this, it will automatically check and list installed images that can be run by this tool.

You will be asked to:

**Step 1**. Select one or more Docker images you want to run.

**Step 2**. Select one model, or specify the model path (abs path needed).

**Step 3**. Set inference arguments: `-i`,`-t`,`-p`... (Optional)

*e.g. In **Step 3**, input `-n 256 -i "Once upon a time"`, then all selected images will inference model with `step=256, prompt="Once upon a time"` .*

Then the tool will run all your selected images, with args your set. And you will see stdout from all those running containers (images), with arg status and inference result printed, looks like:
![run_img](https://github.com/user-attachments/assets/b92ba884-c08d-45e2-9236-1381d56baf2b)



[Back to Shortcuts](#shortcuts)
#### Run Image in Single Command
A faster way to run a specific image is to call `run_img` action with specified `image_tag` and `model_path`, followed by inference args if needed.
```bash
llama-deck run_img <image_tag> <model_path> <other args (optional)>
```
For example, if I want to:
1. Inference the model: `/home/bufan/LlamaDeckResources/llamaModels/stories15M.bin`
2. run [llama2.java](https://github.com/mukel/llama2.java) inside image with tag 'llama2.java_mukel'
3. 128 steps and prompt "Once upon a time"

Then the command is:
```bash
llama-deck run_img llama2.java_mukel \
/home/bufan/LlamaDeckResources/llamaModels/stories15M.bin \
-n 128 -i "Once opon a time"
```
Result:
```bash
$ llama-deck run_img llama2.java_mukel /home/bufan/LlamaDeckResources/llamaModels/stories15M.bin  -n 128 -i "Once opon a time"

==> Selected run arguments:
image_tag: llama2.java_mukel
model_path: /home/bufan/LlamaDeckResources/llamaModels/stories15M.bin
steps: 128
input_prompt: Once opon a time


Running llama2.java_mukel...

################## stdout from llama2.java_mukel ####################

==>Supported args:
tokenizer
prompt
chat_init_prompt
mode
temperature
step
top-p
seed

==> Set args:
prompt = 'Once opon a time'
step = 128

==> RUN COMMAND: java --enable-preview --add-modules=jdk.incubator.vector Llama2 /models/model.bin  -i 'Once opon a time'    -n 128  
WARNING: Using incubator modules: jdk.incubator.vector
Config{dim=288, hidden_dim=768, n_layers=6, n_heads=6, n_kv_heads=6, vocab_size=32000, seq_len=256, shared_weights=true, head_size=48}
Once opon a time, there was a boy. He liked to throw a ball. Every day, he would go outside and throw the ball with his friends.
One day, the boy saw something funny. He saw a penny, made of copper and was very happy. He liked the penny so much that he wanted to throw it again.
He threw the penny and tried to make it go even higher. But, the penny was too lazy to go higher. So, the boy went back to the penny and tried again. He threw it as far as he could.
But this time

achieved tok/s: 405.750799
#####################################################################

All images finished.
```

**IMPORTANT!** Please always give the absolute path when inputing the `<model_path>`: Since the llama model file is always large, instead of copying it into each container and improve IO and memory cost, `llama-deck` choose to mount the model into each running container (image), where absolute path is needed to mount it when starting an image.

[Back to Shortcuts](#shortcuts)

#### More about passing inference arguments ####

Inference args supported by `llama-deck` are the same as [llama2.c](https://github.com/karpathy/llama2.c). Those are:

`-t <float>`  temperature in [0,inf], default 1.0

`-p <float>`  p value in top-p (nucleus) sampling in [0,1] default 0.9

`-s <int>`    random seed, default time(NULL)

`-n <int>`    number of steps to run for, default 256. 0 = max_seq_len

`-i <string>` input prompt

`-z <string>` optional path to custom tokenizer (not implemented yet)

`-m <string>` mode: generate|chat, default: generate

`-y <string>` (optional) system prompt in chat mode

It is noticed that not all implementations supports all these args from [llama2.c](https://github.com/karpathy/llama2.c). And due to the nature of different implementations, different ways/formats are used to pass these args. 

So for each selected image to run, `llama-deck` will automatically detect its supported args and drop out those unsupported. Then it convert args you set into correct format, put it to correct position (in a command to run the implementation) and finally pass them to inplementation inside the image. This operation is done inside each running container.

[Back to Shortcuts](#shortcuts)

### Available Images

-------------------------------------------------------------------------------------------------------------------------

|    | Tag                 | Size     | Author    | Repository                             |
|---:|:--------------------|:---------|:----------|:---------------------------------------|
|  1 | llama2.zig_cgbur    | 259.0 MB | @cgbur    | https://github.com/cgbur/llama2.zig    |
|  2 | llama2.cs_trrahul   | 374.0 MB | @trrahul  | https://github.com/trrahul/llama2.cs   |
|  3 | llama2.py_tairov    | 57.0 MB  | @tairov   | https://github.com/tairov/llama2.py    |
|  4 | llama2.rs_gaxler    | 331.0 MB | @gaxler   | https://github.com/gaxler/llama2.rs    |
|  5 | llama2.c_karpathy   | 139.0 MB | @karpathy | https://github.com/karpathy/llama2.c   |
|  6 | llama2.java_mukel   | 178.0 MB | @mukel    | https://github.com/mukel/llama2.java   |
|  7 | go-llama2_tmc       | 133.0 MB | @tmc      | https://github.com/tmc/go-llama2       |
|  8 | llama2.cpp_leloykun | 169.0 MB | @leloykun | https://github.com/leloykun/llama2.cpp |

-------------------------------------------------------------------------------------------------------------------------

More dockerized implementations will be extended.

[See our image repository](https://hub.docker.com/r/bufan0222/ll_implements/tags).


# TODO List
1. Implement customized tokenizer when running images.
2. Extend more models and build more images.
3. Try Multi-thread in running images?

# License
See the LICENSE file for details.

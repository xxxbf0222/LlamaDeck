# LlamaGymCLI

**Llama Shepherd** is a command-line tool for quickly managing and experimenting with multiple versions of llama inference implementations. It can help you quickly filter and download [different llama implementations](#available-repositories)) and [llama2-like transformer-based LLM models](#available-models). We also provide [some images](#available-images) based on some implementations, which can be easily deploy and run through our tool. Inspired by [llama2.c project](https://github.com/karpathy/llama2.c).

## Shortcuts
[Install The Tool](#install): `pip install llama-gym`

[Manage Repositories](#explore--download-llama-repositories) : `list_repo` `install_repo` `-l <language>`

[Manage Models](#explore--download-models): `list_model` `install_model`
`-m <model_name>`

[Manage and Run Images](#install--run-images) :`install_img` `run_img`

## Install 
To install the tool, simply run:
```bash
pip install llama-gym
```

## Explore & Download Llama Repositories
![list repositories](https://github.com/user-attachments/assets/1d0d347f-c79f-4f63-8e09-ae07a8662ebd)

### List Repositories
To list all Llama Implementations, run:
```bash
llama-gym list_repo
```
You can also set `-l` to specify the language of the repository, like:
```bash
$ llama-gym list_repo -l java

-------------------------------------------------------------------------------------------------------------------------

|    | language   | name                  | url                                                  | author       |
|---:|:-----------|:----------------------|:-----------------------------------------------------|:-------------|
|  1 | Java       | llama2.java           | https://github.com/mukel/llama2.java                 | @mukel       |
|  2 | Java       | llama2.tornadovm.java | https://github.com/mikepapadim/llama2.tornadovm.java | @mikepapadim |
|  3 | Java       | Jlama                 | https://github.com/tjake/Jlama                       | @tjake       |
|  4 | Java       | llama2j               | https://github.com/LastBotInc/llama2j                | @lasttero    |

-------------------------------------------------------------------------------------------------------------------------
```

### Download Repositories
![install repositories](https://github.com/user-attachments/assets/dc12703a-a960-4044-8eef-6619fa553569)

You can also download those [implementation repositories](#repository-list) through our tool:
```bash
llama-gym install_repo
```

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
llama-gym list_model
```
And for download model:
```bash
llama-gym install_model
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
### Install Images
### Run Images
### Available Images

-------------------------------------------------------------------------------------------------------------------------

|    | Tag                 | Size     | Author    | Repository                             |
|---:|:--------------------|:---------|:----------|:---------------------------------------|
|  1 | llama2.rs_gaxler    | 331.0 MB | @gaxler   | https://github.com/gaxler/llama2.rs    |
|  2 | llama2.c_karpathy   | 139.0 MB | @karpathy | https://github.com/karpathy/llama2.c   |
|  3 | llama2.java_mukel   | 178.0 MB | @mukel    | https://github.com/mukel/llama2.java   |
|  4 | go-llama2_tmc       | 133.0 MB | @tmc      | https://github.com/tmc/go-llama2       |
|  5 | llama2.cpp_leloykun | 169.0 MB | @leloykun | https://github.com/leloykun/llama2.cpp |

-------------------------------------------------------------------------------------------------------------------------

[See our image repository](https://hub.docker.com/r/bufan0222/ll_implements/tags)


# License
This project is licensed under the MIT License - see the LICENSE file for details.

# config.py
default_tokenizer = "https://github.com/karpathy/llama2.c/raw/master/tokenizer.bin"

image_repo = "https://registry.hub.docker.com/v2/repositories/bufan0222/ll_implements/tags"

user_defined_resources_path = ""

repo_options = [

{'language': 'C', 'name': 'llama2.c', 'url': 'https://github.com/karpathy/llama2.c', 'author': '@karpathy'} ,
# Add other C implementations here.



{'language': 'Rust', 'name': 'llama2.rs', 'url': 'https://github.com/gaxler/llama2.rs', 'author': '@gaxler'} ,

{'language': 'Rust', 'name': 'llama2.rs', 'url': 'https://github.com/leo-du/llama2.rs', 'author': '@leo-du'} ,

{'language': 'Rust', 'name': 'llama2-rs', 'url': 'https://github.com/danielgrittner/llama2-rs', 'author': '@danielgrittner'} ,

{'language': 'Rust', 'name': 'llama2.rs', 'url': 'https://github.com/lintian06/llama2.rs', 'author': '@lintian06'} ,

{'language': 'Rust', 'name': 'pecca.rs', 'url': 'https://github.com/rahoua/pecca-rs', 'author': '@rahoua'} ,

{'language': 'Rust', 'name': 'llama2.rs', 'url': 'https://github.com/flaneur2020/llama2.rs', 'author': '@flaneur2020'} ,
# Add other Rust implementations here.



{'language': 'Go', 'name': 'go-llama2', 'url': 'https://github.com/tmc/go-llama2', 'author': '@tmc'} ,

{'language': 'Go', 'name': 'llama2.go', 'url': 'https://github.com/nikolaydubina/llama2.go', 'author': '@nikolaydubina'} ,

{'language': 'Go', 'name': 'llama2.go', 'url': 'https://github.com/haormj/llama2.go', 'author': '@haormj'} ,

{'language': 'Go', 'name': 'llama2.go', 'url': 'https://github.com/saracen/llama2.go', 'author': '@saracen'} ,
# Add other Go implementations here.



{'language': 'Android', 'name': 'llama2.c-android', 'url': 'https://github.com/Manuel030/llama2.c-android', 'author': '@Manuel030'} ,

{'language': 'Android', 'name': 'llama2.c-android-wrapper', 'url': 'https://github.com/celikin/llama2.c-android-wrapper', 'author': '@celikin'} ,
# Add other Android implementations here.



{'language': 'C++', 'name': 'llama2.cpp', 'url': 'https://github.com/leloykun/llama2.cpp', 'author': '@leloykun'} ,

{'language': 'C++', 'name': 'llama2.cpp', 'url': 'https://github.com/coldlarry/llama2.cpp', 'author': '@coldlarry'} ,
# Add other C++ implementations here.



{'language': 'CUDA', 'name': 'llama_cu_awq', 'url': 'https://github.com/ankan-ban/llama_cu_awq', 'author': '@ankan-ban'} ,
# Add other CUDA implementations here.



{'language': 'JavaScript', 'name': 'llama2.js', 'url': 'https://github.com/epicure/llama2.js', 'author': '@epicure'} ,

{'language': 'JavaScript', 'name': 'llamajs', 'url': 'https://github.com/agershun/llamajs', 'author': '@agershun'} ,

{'language': 'JavaScript', 'name': 'llama2.ts', 'url': 'https://github.com/wizzard0/llama2.ts', 'author': '@oleksandr_now'} ,

{'language': 'JavaScript', 'name': 'llama2.c-emscripten', 'url': 'https://github.com/gohai/llama2.c-emscripten', 'author': '@gohai'} ,
# Add other JavaScript implementations here.



{'language': 'Zig', 'name': 'llama2.zig', 'url': 'https://github.com/cgbur/llama2.zig', 'author': '@cgbur'} ,

{'language': 'Zig', 'name': 'llama2.zig', 'url': 'https://github.com/vodkaslime/llama2.zig', 'author': '@vodkaslime'} ,

{'language': 'Zig', 'name': 'llama2.zig', 'url': 'https://github.com/clebert/llama2.zig', 'author': '@clebert'} ,
# Add other Zig implementations here.



{'language': 'Julia', 'name': 'llama2.jl', 'url': 'https://github.com/juvi21/llama2.jl', 'author': '@juvi21'} ,
# Add other Julia implementations here.



{'language': 'Scala', 'name': 'llama2.scala', 'url': 'https://github.com/jrudolph/llama2.scala', 'author': '@jrudolph'} ,
# Add other Scala implementations here.



{'language': 'Java', 'name': 'llama2.java', 'url': 'https://github.com/mukel/llama2.java', 'author': '@mukel'} ,

{'language': 'Java', 'name': 'llama2.tornadovm.java', 'url': 'https://github.com/mikepapadim/llama2.tornadovm.java', 'author': '@mikepapadim'} ,

{'language': 'Java', 'name': 'Jlama', 'url': 'https://github.com/tjake/Jlama', 'author': '@tjake'} ,

{'language': 'Java', 'name': 'llama2j', 'url': 'https://github.com/LastBotInc/llama2j', 'author': '@lasttero'} ,
# Add other Java implementations here.



{'language': 'Kotlin', 'name': 'llama2.kt', 'url': 'https://github.com/madroidmaq/llama2.kt', 'author': '@madroidmaq'} ,
# Add other Kotlin implementations here.



{'language': 'Python', 'name': 'llama2.py', 'url': 'https://github.com/tairov/llama2.py', 'author': '@tairov'} ,
# Add other Python implementations here.



{'language': 'C#', 'name': 'llama2.cs', 'url': 'https://github.com/trrahul/llama2.cs', 'author': '@trrahul'} ,
# Add other C# implementations here.



{'language': 'Dart', 'name': 'llama2.dart', 'url': 'https://github.com/yiminghan/llama2.dart', 'author': '@yiminghan'} ,
# Add other Dart implementations here.



{'language': 'Web', 'name': 'llama2c-web', 'url': 'https://github.com/dmarcos/llama2.c-web', 'author': '@dmarcos'} ,
# Add other Web implementations here.



{'language': 'WebAssembly', 'name': 'icpp-llm', 'url': 'https://github.com/icppWorld/icpp-llm', 'author': '@icppWorld'} ,
# Add other WebAssembly implementations here.



{'language': 'Fortran', 'name': 'llama2.f90', 'url': 'https://github.com/rbitr/llama2.f90', 'author': '@rbitr'} ,
# Add other Fortran implementations here.



{'language': 'Mojo', 'name': 'llama2.🔥', 'url': 'https://github.com/tairov/llama2.mojo', 'author': '@tairov'} ,
# Add other Mojo implementations here.



{'language': 'OCaml', 'name': 'llama2.ml', 'url': 'https://github.com/jackpeck/llama2.ml', 'author': '@jackpeck'} ,
# Add other OCaml implementations here.



{'language': 'Everywhere', 'name': 'llama2.c', 'url': 'https://github.com/trholding/llama2.c', 'author': '@trholding'} ,
# Add other Everywhere implementations here.



{'language': 'Bilingual', 'name': 'llama2.c-zh', 'url': 'https://github.com/chenyangMl/llama2.c-zh', 'author': '@chenyangMl'} ,
# Add other Bilingual implementations here.

]

model_options = [
    {'Model': 'stories15M', 'url': 'https://huggingface.co/karpathy/tinyllamas/resolve/main/stories15M.bin'},

    {'Model': 'stories42M', 'url': 'https://huggingface.co/karpathy/tinyllamas/resolve/main/stories42M.bin'},

    {'Model': 'stories110M', 'url': 'https://huggingface.co/karpathy/tinyllamas/resolve/main/stories110M.bin'},

    {'Model': 'Meta-Llama', 'url':'https://llama.meta.com/llama-downloads/'}
]



# 程序

以某个模板新建一个文件，避免每次新建同类文件时输入过多相同的内容。

# 使用
1. 直接使用命令行第一个参数作为文件名

    ``` shell
    python new.py new_File_name
    ```
    若无配置，则默认输出一个空文件，与touch的行为一致。

2. 程序使用~/Templates作为模板以及配置存放文件夹

    其中.config.json为配置文件，其余均默认为模板文件。.config.json格式为json格式，包含多个键值对，表示某个扩展名所对应的文件模板。

    键值emptyFile表示找不到扩展名或者找不到对应文件时默认使用的文件。

3. makefile

    makefile中使用pyinstaller作为python打包工具。make install会将生成的可执行文件拷贝到目录~/bin中。

# 例子
模板文件.config.json如下。
``` json
{
	"py"		: "python",
	"html"		: "html",
	"emptyFile"	: "emptyFile"
}
```
表示*.py新建时拷贝~/Templates/python文件至目标，但是不会覆盖原有文件。

``` shell
$ python new.py another.py
===
$ cp ~/Templates/python another.py

$ python new.py index.html
===
$ cp ~/Templates/html index.html
```

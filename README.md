# shadwoverse-auto-unpack
auto unpack shadowverse character u3d

#HOW TO INSTALL
1.download the repo
2.unzip it
3.install python(I'm using python3.7)
(optional)make a virtualenv
4.open cmd and type"cd {the repo folder path}"
5.type"pip install -r requirements.txt"
6.type"git clone https://github.com/tellowkrinkle/UnityPack"
7.type"python setup.py install"
8.install done

#HOW TO USE
1.make a id folder inside "static" folder(EX:static/2807)
2.put your "ui_class_2807.unity3d" inside the folder
3.open cmd and type "python unpack.py"
4.input your id(EX:2807)
5.The original character image will saved as `"class_{id}_O.png"`
6.The original character alpha image will saved as `"class_{id}_A.png"`
7.The character image + alpha image will saved as `class_{id}.png`
8.The atlas will save as `class_{id}.atlas`
9.The json will save as `class_{id}.json`

#TODO
- [ ] make it to exe 
# py-c-demo
python c++ extends demo

Linux:
```
gcc -fPIC -c test.c 
gcc -shared -o test.so test.o
```

Windows:
用宇宙第一战舰visual studio 2017新建一个DLL项目，把这两个c++文件丢进去编译即可。
报错一般是sdk没装好，把Windows平台开发，使用c++桌面开发勾上安装就好。

使用：   
在Window，把test.py放在test.dll的同目录运行    
在Linux中，加载的路径需要指定为绝对路径。    

## 打包ckpe模块whl包使用方式

1. ##### 获取whl包

![image-20240111094925904](C:\Users\Michael\AppData\Roaming\Typora\typora-user-images\image-20240111094925904.png)

2. ##### pip安装

```
pip install C:\Users\Michael\Desktop\ckpe\ckpe\dist\ckpe-0.1.0-py3-none-any.whl
```

3. ##### 导包实现

```
from ckpe import ckpe

ckpe_obj = ckpe(model_name='微调模型路径', user_dict='字典路径')
```

4. ##### 例子

```
if __name__ == '__main__':
    text = 'APS理论和劳动生产率、维修成本之间的关系是什么？'
    key_phrase = ckpe_obj.extract_keyphrase(text, top_k=-1, with_weight=True)
    print(key_phrase)
```

##### 5. 结果

```
[('维修成本', 2.8802847535928104), ('劳动生产率', 0.9178460080331394), ('理论', 0.7155251233118518), ('关系', 0.5773353009767901)]
```





## 打包ckpe模块whl包打包方式

##### 详情：打包成`whl`,然后用pip进行本地安装

##### 安装setuptools

```python
pip install setuptools
```

##### pytorch文件tree

<img src="C:\Users\Michael\AppData\Roaming\Typora\typora-user-images\image-20240111100251410.png" alt="image-20240111100251410" style="zoom:67%;" />

##### 创建setup.py文件

```
from setuptools import setup, find_packages

setup(
    name='ckpe',
    version='0.1.0',
    description='python toolkit',
    url='https://github.com/jesuswa/ckpe.git',
    author='wh-ckpe01',
    author_email='13673146262@163.com',
    license='MIT',
    keywords='python toolkit utils',
    packages=find_packages(),  # 这会自动找到所有子包
    package_data={
        # 如果你有在任何包下的文件夹中的文件需要包含进来，可以这样指定
        '': ['*.txt', '*.json'],  # 包括所有目录下的.txt和.json文件
    },
    include_package_data=True,  # 这告诉setuptools包含那些在MANIFEST.in中指定的文件
    install_requires=[
        'pkuseg',  # 确保这是你项目需要的依赖包
    ],
    python_requires='>=3',
)
```

##### 生成whl

```
python setup.py bdist_wheel
```

<img src="C:\Users\Michael\AppData\Roaming\Typora\typora-user-images\image-20240111100855970.png" alt="image-20240111100855970" style="zoom:67%;" />



#### 调研地址：

##### 主要是 - setup编写



[如何制作并使用python发布的模块压缩包和whl包，并进行pip安装和使用教程，加上传Pypi，上传之后又如何增删whl项目_python制作发布压缩包-CSDN博客](https://blog.csdn.net/qq_41375318/article/details/115568827)

[如何制作并使用python发布的模块压缩包和whl包，并进行pip安装和使用教程_哔哩哔哩_bilibili](https://www.bilibili.com/video/BV1iK4y1K7B6/?spm_id_from=333.337.search-card.all.click&vd_source=e3df572c4d8a63ddc28cad70680f8ca1)
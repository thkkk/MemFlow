from setuptools import setup, find_packages
import sys

# 检查Python版本和系统要求（FlashAttention需要Linux或部分Windows支持）
if sys.platform not in ["linux", "win32"]:
    raise RuntimeError("FlashAttention only supports Linux and limited Windows support (see GitHub issues)")

# 核心依赖配置
install_requires = [
    # 基础科学计算库
    'numpy>=1.21.0',
    'scipy>=1.7.0',
    'matplotlib>=3.0.0',
    
    # 图像处理相关
    'opencv-python>=4.5.0',
    'imageio>=2.15.0',
    'Pillow>=9.0.0',  # 隐式依赖项
    
    # 深度学习框架
    'torch>=2.2.0',  # FlashAttention的硬性要求
    
    # 实用工具
    'tqdm>=4.0.0',
    'loguru>=0.7.0',
    'h5py>=3.0.0',
    'yacs>=0.1.8',
    
    # 数据处理
    'einops>=0.6.0',
    'pandas>=1.0.0',  # 隐式依赖项
    
    # FlashAttention的显式依赖
    'packaging>=21.0',
    'ninja>=1.11.1'
]

# 条件依赖（timm特定版本）
extras_require = {
    'timm': ['timm>=0.4.12'],
    'flash-attn': ['flash-attn>=2.3.2']
}

# 系统特定的依赖处理
if sys.platform == "linux":
    install_requires.extend([
        'cuda-python>=11.0'  # 可选，但推荐用于CUDA版本检查
    ])

setup(
    name="MemFlow",
    version="0.1.0",
    author="thkkk",
    author_email="tanhengkai@qq.com",
    description="MemFlow",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/thkkk/MemFlow",
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=install_requires,
    extras_require=extras_require,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Artificial Intelligence"
    ],
    # FlashAttention的特殊构建选项
    dependency_links=[],
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'memflow=memflow.module:main',
        ],
    }
)
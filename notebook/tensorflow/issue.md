# 编译问题

### pip安装由于编译好的二进制文件性能不足 提醒自行编译安装

Your CPU supports instructions that this TensorFlow binary was not compiled to use: SSE4.1 SSE4.2 AVX AVX2 FMA
    
    # Just disables the warning, doesn't enable AVX/FMA
    import os
    os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
    
or by setting export TF_CPP_MIN_LOG_LEVEL=2 if you're on Unix. Tensorflow is working fine anyway, but you won't see these annoying warnings.
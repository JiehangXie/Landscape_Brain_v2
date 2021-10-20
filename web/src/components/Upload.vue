<script>
import { ElMessage } from 'element-plus'

export default ({
    setup() {
        
    },
    methods:{
      upload_process() {
          ElMessage('数据上传中……');
        },
      upload_error(){
          ElMessage.error('数据上传错误！');
      },
      upload_success(){
        ElMessage.success({
            message: '数据上传成功！',
            type: 'success'
          });
        location.reload();
      }
    }
})
</script>

<template>
    <el-upload
        class="upload-image"
        action="http://lhs.gis.show:5000/api/upload/v1/"
        :on-progress="upload_process"
        :on-success="upload_success"
        :on-error="upload_error"
        :limit="1"
    >
        <div id="background-img"></div>
    </el-upload>

    
</template>

<style>
body {
    margin:0;
    
}

.el-upload--text{
    display:block;
}
.el-upload-list{
    display: none;
}


#background-img{
    background: url("../assets/backimg.jpg");
    background-size: 100% 100%;
    height: 100%;
    position: fixed;
    width: 100%
}
</style>
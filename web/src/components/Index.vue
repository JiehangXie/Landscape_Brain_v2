<template>
<el-container>
    <!--顶部导航-->
    <el-header>
        <el-menu
            :default-active="activeIndex"
            class="el-menu-demo"
            mode="horizontal"
            @select="handleSelect"
        >
        <el-menu-item index="1">
        <svg t="1632956848237" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="3306" width="50" height="50"><path d="M512 208a101.12 101.12 0 0 1 201.386667-13.013333A170.666667 170.666667 0 0 1 853.333333 362.666667a164.053333 164.053333 0 0 1 0 17.706666 213.333333 213.333333 0 0 1 0 306.133334 157.226667 157.226667 0 0 1 0 17.493333 149.333333 149.333333 0 0 1-136.746666 149.333333A106.666667 106.666667 0 0 1 512 810.666667z" fill="#A9B8C0" p-id="3307"></path><path d="M512 208a101.12 101.12 0 0 0-201.386667-13.013333A170.666667 170.666667 0 0 0 170.666667 362.666667a164.053333 164.053333 0 0 0 0 17.706666 213.333333 213.333333 0 0 0 0 306.133334A157.226667 157.226667 0 0 0 170.666667 704a149.333333 149.333333 0 0 0 136.746666 149.333333A106.666667 106.666667 0 0 0 512 810.666667z" fill="#C3CED3" p-id="3308"></path><path d="M512 704a62.72 62.72 0 0 1-64 64v42.666667a106.666667 106.666667 0 0 0 106.666667-106.666667zM341.333333 405.333333h42.666667a62.72 62.72 0 0 1 64-64v-42.666666a62.72 62.72 0 0 1-64-64h-42.666667a105.386667 105.386667 0 0 0 42.666667 85.333333 105.386667 105.386667 0 0 0-42.666667 85.333333zM426.666667 512h-42.666667c0 45.653333-26.026667 62.72-49.28 64A230.826667 230.826667 0 0 0 234.666667 554.666667v42.666666c76.16 0 126.933333 31.36 150.826666 93.013334l39.68-15.36a181.546667 181.546667 0 0 0-46.08-69.12A102.4 102.4 0 0 0 426.666667 512z" fill="#A9B8C0" p-id="3309"></path><path d="M710.613333 405.333333c-23.253333 0-49.28-18.133333-49.28-64h-42.666666a102.4 102.4 0 0 0 47.573333 93.866667 181.546667 181.546667 0 0 0-46.08 69.12l39.68 15.36C683.733333 458.026667 734.506667 426.666667 810.666667 426.666667v-42.666667a230.826667 230.826667 0 0 0-100.053334 21.333333zM512 490.666667h-42.666667a106.666667 106.666667 0 0 0 106.666667 106.666666v-42.666666a62.72 62.72 0 0 1-64-64zM704 640h-42.666667a62.72 62.72 0 0 1-64 64v42.666667a62.72 62.72 0 0 1 64 64h42.666667a105.386667 105.386667 0 0 0-42.666667-85.333334 105.386667 105.386667 0 0 0 42.666667-85.333333z" fill="#C3CED3" p-id="3310"></path></svg>        <a class="menu-title">Landscape Brain</a></el-menu-item>
        </el-menu>
        <div class="line"></div>
    </el-header>
    <!--侧栏导航-->
    <el-container>
        <el-aside>
            <el-menu
                default-active="1"
                class="el-menu-vertical"
                :collapse="true"

            >
                <el-menu-item index="1">
                <i class="el-icon-s-data"></i>
                <template #title>数据列表</template>
                </el-menu-item>
                <el-menu-item index="2">
                <i class="el-icon-upload"></i>
                <template #title>手动上传图片</template>
                </el-menu-item>
                <el-menu-item index="3" disabled>
                <i class="el-icon-setting"></i>
                <template #title>设置</template>
                </el-menu-item>
            </el-menu>
        </el-aside>

        <!--页面主内容scope.row.img_url-->
        <el-main>
            <!--表格-->
              <el-table
                :data="dataList"
                style="width: 100%"
            >
                <el-table-column prop="img_code" label="图像编码" width="180" align="center" />

                <!--图片展示开始-->
                <el-table-column label="图片" width="180" align="center">
                    <template #default="scope">
                          <el-button type="text" @click="original_image_button(scope.row.img_url)">原图</el-button>
                          <el-button type="text" @click="original_image_button(scope.row.label_img_url)">效果图</el-button>
                          <el-dialog v-model="ImageDialogVisible" title="查看图片">
                                  <el-image
                                    :src="dialog_img_url"
                                    :fit="contain"
                                ></el-image>
                          </el-dialog>
                    </template>
                </el-table-column>
                <!--图片展示结束-->

                <el-table-column prop="time" label="采集时间" :formatter="dateFormat" width="150" align="center" />

                <!--地图开始-->
                <el-table-column prop="loc_lat" label="采集坐标" width="180" align="center">
                    <template #default="scope">
                        <el-button type="text" @click="map_button(scope.row.loc_lng,scope.row.loc_lat)"><i class="el-icon-coordinate"></i>查看位置</el-button>
                          <el-dialog v-model="MapDialogVisible" title="查看位置">
                                <el-image
                                    :src="map_img_url"
                                    :fit="contain"
                                ></el-image>
                          </el-dialog>
                    </template>
                </el-table-column>
                <!--地图结束-->

                <el-table-column prop="building" label="建筑率" width="90" align="center"/>
                <el-table-column prop="green" label="绿视率" width="90" align="center" />
                <el-table-column prop="sky" label="天空比" width="90" align="center" />
                <el-table-column prop="score" label="健康景观评分" width="120" align="center" />
                

                <!--评分建议开始-->
                <el-table-column label="改善建议" fixed="right" align="center">
                    <template #default="scope">
                        <el-alert v-if="scope.row.advice==0" title="该景观节点基本符合健康景观标准。" type="success" show-icon :closable="false"> </el-alert>
                        <el-alert v-if="scope.row.advice==1" title="该景观节点植物覆盖不足！" type="warning" show-icon :closable="false"> </el-alert>
                        <el-alert v-if="scope.row.advice==2" title="该景观节点可能存在采光不足的情况！" type="warning" show-icon :closable="false"> </el-alert>
                        <el-alert v-if="scope.row.advice==3" title="该景观节点建筑密度过高！" type="warning" show-icon :closable="false"> </el-alert>
                        <el-alert v-if="scope.row.advice==4" title="建议该景观节点增加乔木和提升空间开阔度！" type="warning" show-icon :closable="false"> </el-alert>
                        <el-alert v-if="scope.row.advice==5" title="建议该景观节点增加植物覆盖和减少建筑密度！" type="warning" show-icon :closable="false"> </el-alert>
                        <el-alert v-if="scope.row.advice==6" title="该景观节点存在建筑密度过高和采光不足的问题！" type="warning" show-icon :closable="false"> </el-alert>
                        <el-alert v-if="scope.row.advice==7" title="该景观节点问题突出，建议增加植物、控制建筑密度和改善采光条件！" type="warning" show-icon :closable="false"> </el-alert>
                    </template>
                </el-table-column>
                <!--评分建议结束-->
            </el-table>
        </el-main>

    </el-container>
    <!--页尾-->
    <el-footer>
        <div class="copyright">&copy;JackieTse  <a href="https://github.com/JiehangXie/Landscape_Brain_v2" target="blank">(Github)</a> 2021</div>
    </el-footer>
</el-container>
</template>

<script>
import axios from 'axios'
import moment from 'moment'
export default{
    data(){
        return {
            dataList_URL:"http://lhs.gis.show:5000/api/v1/",
            dataList:[],
            ImageDialogVisible: false,
            MapDialogVisible: false,
        }
    },
    created(){
        axios.get(this.dataList_URL).then((res)=>{
            this.dataList = res.data;
        })
    },
    mounted(){
        window.Vue = this;
    },
    methods:{
        original_image_button(img_path){
            this.dialog_img_url = img_path;
            this.ImageDialogVisible = true;
        },

        map_button(lng,lat){
            this.map_img_url = 'https://api.map.baidu.com/staticimage/v2?ak=hmy7eqL2XgsOnqDsmgoydP1bLtOtw56x&width=900&height=540&zoom=18&coordtype=wgs84ll&markerStyles=l,,0xFF0000&markers=' + lng + ',' + lat;
            this.MapDialogVisible = true;

        },

        dateFormat(row, column) {
        var date = Number(row[column.property]);
        if (date == undefined) {
            return "";
        }
        return moment(date).format("YYYY-MM-DD HH:mm");
        },


    },
}

</script>

<style scoped>
.menu-title{
    font-size: 20px;
    font-weight: bold;
    margin-left: 10px;
}
.el-menu-vertical {
    height: 870px;
}
.el-aside{
    width:80px;
}
.copyright{
    text-align: center;
}
</style>

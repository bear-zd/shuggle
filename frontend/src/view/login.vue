<!--<template>-->
<!--  <title>登录</title>-->
<!--  <div class="login">-->
<!--    <h4>shuggle登录</h4>-->
<!--    <el-form :label-position=center-->
<!--             lebel-width="80px"-->
<!--    >-->
<!--      <el-form-item label="电子邮箱">-->
<!--        <el-input type="text"-->
<!--                  placeholder="请输入电子邮箱"-->
<!--                  v-model="email">-->
<!--        </el-input>-->
<!--      </el-form-item>-->
<!--      <el-form-item label="密码">-->
<!--        <el-input type="password"-->
<!--                  placeholder="请输入密码"-->
<!--                  v-model="password"-->
<!--                  show-password>-->
<!--        </el-input>-->
<!--      </el-form-item>-->
<!--      <el-form-item>-->
<!--        <el-button @click="login_btn" class="btn_login" type="primary">-->
<!--          登录-->
<!--        </el-button>-->
<!--      </el-form-item>-->
<!--    </el-form>-->
<!--  </div>-->
<!--  <router-view/>-->
<!--</template>-->
<template>
  <h1>what a sad</h1>
</template>

<script>

import {ElMessage} from 'element-plus'
// import router from "../router/index.js"
import axios from "axios";
export default {
  name: "login",
  data() {
    return {
      email: "",
      password: "",
    };
  },
  methods: {
    login_btn: function () {
      if (!this.email || !this.password) {
        ElMessage.error("邮箱和密码不能为空")
      } else {
        axios.get("http://localhost:11090/login",
            {params: {email: this.email, password: this.password}})
            .then(function (response) {
              console.log(response);
            })
      }
    }
  }
}
</script>

<style scoped>
.login {
  width: 450px;
  margin: 180px auto;
  border: 1px solid #efefef;
  padding: 20px;
  border-radius: 10px;
}

h4 {
  text-align: center;
}

.btn_login {
  width: 100%;
}

</style>


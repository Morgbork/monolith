<template>
      <v-container
        class="fill-height fix-margin"
        fluid

      >
        <v-row
          align="center"
          justify="center"
        >
          <v-col
            cols="12"
            sm="8"
            md="6"
            lg="4"
          >
            <v-card class="elevation-12">
              <v-toolbar
                color="#424242"
                dark
                flat
              >
                <v-toolbar-title>Login as admin</v-toolbar-title>
              </v-toolbar>
              <v-card-text>
                <v-form>
                  <v-text-field
                    label="Login"
                    name="login"
                    type="text"
                    v-model="login"
                  />

                  <v-text-field
                    id="password"
                    label="Password"
                    name="password"
                    type="password"
                    v-model="password"
                  />
                </v-form>
              </v-card-text>
              <v-card-actions>
                <v-spacer />
                <v-btn dark color="#424242"
                @click="onSubmit">
                  Login
                </v-btn>
              </v-card-actions>
            </v-card>
          </v-col>
        </v-row>
      </v-container>
</template>


<script>
    export default {
        data () {
            return {
              login: '',
                password: ''
            }
        },
        methods: {
            onSubmit (){
              return this.$store.dispatch('ADMIN_AUTH', {login: this.login, email: '', password: this.password})
            }
        }
    }
</script>

<style scoped>
  .fix-margin {
    margin-top: 200px;
  }
</style>

<template>
  <v-content class="mx-12">

    <v-container fluid px-12>
      <v-row align="center">
        <v-col cols="12" sm="6">
          <v-btn large color="green" @click="hiddenForm = !hiddenForm">Add new product</v-btn>
        </v-col>
      </v-row>
      <v-divider></v-divider>
      <v-row align="center" v-bind:class="{inactive: hiddenForm}">
        <v-col cols="12" sm="6">
          <v-text-field
            label="Product code"
            outlined
            color="#424242"
          ></v-text-field>
        </v-col>
        <v-col cols="12" sm="6">
          <v-text-field
            label="Product name"
            outlined
            color="#424242"
          ></v-text-field>
        </v-col>
        <v-col cols="12" sm="6">
          <v-text-field
            label="Category"
            outlined
            color="#424242"
          ></v-text-field>
        </v-col>
        <v-col cols="12" sm="6">
          <v-text-field
            label="Price"
            outlined
            suffix="$"
            color="#424242"
          ></v-text-field>
        </v-col>
        <v-col cols="12">
          <v-textarea
            label="Description"
            outlined
            color="#424242"
          ></v-textarea>
        </v-col>
        <v-col cols="12" sm="4">
          <v-file-input
            label="Product image"
            filled
            prepend-icon="mdi-camera"
          ></v-file-input>
        </v-col>
        <v-col cols="12" sm="8">
          <v-checkbox
            v-model="autoGrow"
            class="ma-1"
            label="In stock"
            color="#424242"
          ></v-checkbox>
        </v-col>
        <v-col cols="1">
          <v-btn large color="green">Submit</v-btn>
        </v-col>
        <v-col cols="1">
          <v-btn large color="red">Cancel</v-btn>
        </v-col>
      </v-row>
      <v-divider></v-divider>
    </v-container>

    <v-container fluid px-12 >
      <v-row align="center">
        <v-col>
          <v-expansion-panels accordion multiple focusable>
            <v-expansion-panel
              v-for="item in goodsList"
              :key="item.id"
            >
              <v-expansion-panel-header>
                <v-container ma-n4>
                  <v-row align="center">
                    {{item.name}} ({{item.product_code}})
                  </v-row>
                </v-container>
              </v-expansion-panel-header>
              <v-expansion-panel-content>
                <v-container fluid px-12>
                  <v-divider></v-divider>
                  <v-row align="center">
                    <v-col cols="12" sm="6">
                      <v-text-field
                        label="Product code"
                        outlined
                        color="#424242"
                      ></v-text-field>
                    </v-col>
                    <v-col cols="12" sm="6">
                      <v-text-field
                        label="Product name"
                        outlined
                        color="#424242"
                      ></v-text-field>
                    </v-col>
                    <v-col cols="12" sm="6">
                      <v-text-field
                        label="Category"
                        outlined
                        color="#424242"
                      ></v-text-field>
                    </v-col>
                    <v-col cols="12" sm="6">
                      <v-text-field
                        label="Price"
                        outlined
                        suffix="$"
                        color="#424242"
                      ></v-text-field>
                    </v-col>
                    <v-col cols="12">
                      <v-textarea
                        label="Description"
                        outlined
                        color="#424242"
                      ></v-textarea>
                    </v-col>
                    <v-col cols="12" sm="4">
                      <v-file-input
                        label="Product image"
                        filled
                        prepend-icon="mdi-camera"
                      ></v-file-input>
                    </v-col>
                    <v-col cols="12" sm="8">
                      <v-checkbox
                        v-model="autoGrow"
                        class="ma-1"
                        label="In stock"
                        color="#424242"
                      ></v-checkbox>
                    </v-col>
                    <v-col cols="1">
                      <v-btn large color="green">Change</v-btn>
                    </v-col>
                    <v-col cols="1" >
                      <v-btn large color="red">Cancel</v-btn>
                    </v-col>
                  </v-row>
                </v-container>
              </v-expansion-panel-content>
            </v-expansion-panel>
          </v-expansion-panels>
        </v-col>
      </v-row>
    </v-container>

  </v-content>
</template>


<script>
    export default {
        data () {
            return {
                hiddenForm: true,
                name: "ggg"
            }
        },
        mounted() {
            this.$store.dispatch('GET_GOODS');
        },
        computed: {
            goodsList() {
                return this.$store.getters.GOODS;
            },
        }
    }
</script>


<style scoped>
  .inactive {
    display: none;
  }
</style>

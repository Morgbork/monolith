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
            v-model="newProduct.product_code"
            label="Product code"
            filled
            color="#424242"
          ></v-text-field>
        </v-col>
        <v-col cols="12" sm="6">
          <v-text-field
            v-model="newProduct.name"
            label="Product name"
            filled
            color="#424242"
          ></v-text-field>
        </v-col>
        <v-col cols="12" sm="6" >
          <v-combobox
            v-model="newProduct.category"
            item-text="category"
            :items="categoriesList"
            label="Category"
            filled
            color="#424242"
          ></v-combobox>
        </v-col>
        <v-col cols="12" sm="6">
          <v-text-field
            v-model="newProduct.price"
            label="Price"
            filled
            suffix="$"
            color="#424242"
          ></v-text-field>
        </v-col>
        <v-col cols="12" sm="6">
          <v-text-field
            v-model="newProduct.manufacturer"
            label="Manufacturer"
            filled
            color="#424242"
          ></v-text-field>
        </v-col>
        <v-col cols="12" sm="6">
          <v-file-input
            v-model="newProduct.image"
            label="Product image"
            filled
            prepend-icon="mdi-camera"
          ></v-file-input>
        </v-col>
        <v-col cols="12">
          <v-textarea
            v-model="newProduct.description"
            label="Description"
            filled
            color="#424242"
          ></v-textarea>
        </v-col>

        <v-col cols="12" sm="4">
          <v-checkbox
            v-model="newProduct.stock"
            class="ma-1"
            label="In stock"
            color="#424242"
          ></v-checkbox>
        </v-col>
        <v-col cols="4">
          <v-btn large color="green" @click="addProduct(newProduct)">Submit</v-btn>
        </v-col>
        <v-col cols="4">
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
                  <v-row align="center">
                    <v-col cols="12" sm="6">
                      <v-text-field
                        v-model="item.product_code"
                        label="Product code"
                        filled
                        placeholder="Product code"
                        color="#424242"
                      ></v-text-field>
                    </v-col>
                    <v-col cols="12" sm="6">
                      <v-text-field
                        v-model="item.name"
                        label="Product name"
                        filled
                        color="#424242"
                      ></v-text-field>
                    </v-col>
                    <v-col cols="12" sm="6">
                      <v-combobox
                        item-text="category"
                        :items="categoriesList"
                        v-model="item.category"
                        label="Category"
                        filled
                        color="#424242"
                      ></v-combobox>
                    </v-col>
                    <v-col cols="12" sm="6">
                      <v-text-field
                        v-model="item.price"
                        label="Price"
                        filled
                        suffix="$"
                        color="#424242"
                      ></v-text-field>
                    </v-col>
                    <v-col cols="12" sm="6">
                      <v-text-field
                        v-model="item.manufacturer"
                        label="Manufacturer"
                        filled
                        color="#424242"
                      ></v-text-field>
                    </v-col>
                    <v-col cols="12" sm="6">
                      <v-file-input
                        label="Product image"
                        filled
                        prepend-icon="mdi-camera"
                      ></v-file-input>
                    </v-col>
                    <v-col cols="12">
                      <v-textarea
                        v-model="item.description"
                        label="Description"
                        filled
                        color="#424242"
                      ></v-textarea>
                    </v-col>
                    <v-col cols="12" sm="4">
                      <v-checkbox
                        checked
                        v-model="item.stock"
                        class="ma-1"
                        label="In stock"
                        color="#424242"
                      ></v-checkbox>
                    </v-col>
                    <v-col cols="4">
                      <v-btn large color="green" @click="updateProduct(item)">Change</v-btn>
                    </v-col>
                    <v-col cols="4" >
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
                newProduct: {}
            }
        },
        mounted() {
            this.$store.dispatch('GET_GOODS');
            this.$store.dispatch('GET_CATEGORIES');
        },
        computed: {
            goodsList() {
                return this.$store.getters.GOODS;
            },
            categoriesList() {
                return this.$store.getters.CATEGORIES;
            },
        },
        methods: {
            addProduct(newProduct) {
                let product = new FormData();
                for (let key in newProduct) {
                    let name = key;
                    let value = newProduct[key];
                    product.append(name, value);
                }
                // for (let i of product.entries()) {
                //     console.log(i[0]+i[1])
                // }
                return this.$store.dispatch('ADD_PRODUCT', product)
            },
            updateProduct(updatedProduct) {
                let product = new FormData();
                for (let key in updatedProduct) {
                    let name = key;
                    let value = updatedProduct[key];
                    if (name === 'updated') {break}
                    product.append(name, value);
                }
                for (let i of product.entries()) {
                    console.log(i[0]+i[1])
                }
                return this.$store.dispatch('UPDATE_PRODUCT', product)
            }
        }
    }
</script>


<style scoped>
  .inactive {
    display: none;
  }
</style>

<template>
  <div>
    <v-app>
      <v-navigation-drawer app color="#424242">
        <v-img max-width="250px" position="center" src="../assets/logo_final_tochno_final_228.png"></v-img>
      </v-navigation-drawer>
      <div class="mb-5">
        <v-toolbar flat>
          <v-toolbar-title>Title</v-toolbar-title>
          <v-spacer></v-spacer>
          <v-toolbar-items>
          </v-toolbar-items>
          <template v-if="$vuetify.breakpoint.smAndUp">
            <v-btn icon>
              <v-icon>mdi-export-variant</v-icon>
            </v-btn>
          </template>
        </v-toolbar>
      </div>
      <v-content class="mx-12">
        <v-carousel >
          <v-carousel-item
            v-for="(color, i) in colors"
            :key="color"
          >
            <v-sheet
              :color="color"
              height="100%"
              tile
            >
              <v-row
                class="fill-height"
                align="center"
                justify="center"
              >
                <div class="display-3">Slide {{ i + 1 }}</div>
              </v-row>
            </v-sheet>
          </v-carousel-item>
        </v-carousel>
        <v-container fluid>
          <v-item-group>
            <v-container>
              <v-row>
                <v-col
                  v-for="n in goodsList"
                  :key="n"
                  cols="12"
                  md="3"
                >
                  <v-item v-slot:default="{ active, toggle }">
                    <v-card
                      class="mx-auto"
                      max-width="400"
                    >
                      <v-card-title>{{n.name}}</v-card-title>
                      <v-img
                        class="white--text align-end"
                        height="200px"
                        :src="n.image"
                      >
                      </v-img>

                      <v-card-text class="text--primary body-1 font-weight-medium">
                        <div>{{n.price}}$</div>
                      </v-card-text>

                      <v-card-actions>
                        <v-btn
                          color="orange"
                          text
                        >
                          Favorite
                        </v-btn>

                        <v-btn
                          color="orange"
                          text
                        >
                          Buy
                        </v-btn>
                      </v-card-actions>
                    </v-card>
                  </v-item>
                </v-col>
              </v-row>
            </v-container>
          </v-item-group>
        </v-container>
      </v-content>
      <v-footer app>
      </v-footer>
    </v-app>
  </div>
</template>


<script>
export default {
    name: 'app',  data() {
        return {
            image_src: require("../assets/logo_final_tochno_final_228.png"),
            msg: "Welcome to Your Vue.js App"
        };
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


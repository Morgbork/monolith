<template>
  <v-content class="mx-12">
    <h1>{{category}}</h1>
    <v-item-group>
      <v-container>
        <v-row justify="left" dense>
          <v-col
            v-for="n in goodsList"
            :key="n.id"
            cols="auto"
          >
            <v-item>
              <v-card
                class="mx-auto"
                max-width="250"
              >
                <v-card-title>{{n.name}}</v-card-title>
                <v-img
                  class="white--text align-end"
                  height="160px"
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
  </v-content>
</template>


<script>
  export  default {
      data () {
          return {
              category: this.$route.params.category
          }
      },
      watch: {
        $route (toR, fromR) {
            this.category = toR.params.category;
            this.$store.dispatch('GET_GOODS', {cat: this.$route.params.category});
        }
      },
      computed: {
          goodsList() {
              return this.$store.getters.GOODS;
          },
      }
  }

</script>

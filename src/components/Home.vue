<template>
  <v-content class="mx-12">
    <v-container fluid px-12>
      <v-container px-2>
        <v-carousel>
          <v-carousel-item
          >
            <v-sheet
              height="100%"
              tile
            >
              <v-row
                class="fill-height"
                align="center"
                justify="center"
              >
                <div class="display-3">Slide</div>
              </v-row>
            </v-sheet>
          </v-carousel-item>
        </v-carousel>
      </v-container>

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

    </v-container>
  </v-content>
</template>


<script>
    export default {
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

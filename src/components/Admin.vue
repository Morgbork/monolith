<template>
  <v-content class="mx-12">
    <v-container fluid px-12>
      <v-row align="center">
        <v-expansion-panels accordion multiple focusable>
          <v-expansion-panel
            v-for="item in goodsList"
            :key="item.id"
          >
            <v-expansion-panel-header>
              <v-container ma-n4>
                <v-row align="center" justify="space-between" >
                  {{item.name}}
                </v-row>
              </v-container>
            </v-expansion-panel-header>
            <v-expansion-panel-content>
              Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
            </v-expansion-panel-content>
          </v-expansion-panel>
        </v-expansion-panels>
      </v-row>
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

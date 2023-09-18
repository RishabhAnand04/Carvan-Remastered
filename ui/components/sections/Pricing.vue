<template>
  <section :class="$vuetify.theme.dark ? 'black' : 'white'" class="py-16">
    <v-container>
      <v-row>
        <v-col>
          <v-row no-gutters>
            <v-col class="text-center">
              <div class="text-center">
                <v-btn-toggle
                  v-model="planDuration"
                  active-class="primary darken-1"
                  borderless
                  mandatory
                  light
                  color="white"
                >
                  <v-btn value="monthly"> Monthly Plan </v-btn>
                  <v-btn value="yearly"> Yearly Plan </v-btn>
                </v-btn-toggle>
              </div>
            </v-col>
          </v-row>
        </v-col>
      </v-row>
    </v-container>
    <v-container fluid>
      <v-row class="mx-auto" style="max-width: 1200px">
        <v-col v-for="(plan, ix) in plans" :key="`plan-${ix}`" cols="12" md="4">
          <v-hover v-slot="{ hover }">
            <v-card
              :elevation="hover ? 24 : plan.elevation"
              :color="plan.color"
              max-width="400"
              :class="hover ? 'zoom' : 'notzoom'"
              class="mx-auto transition-swing"
            >
              <h3
                class="text-h4 text-center font-weight-black white--text pt-5"
                v-text="plan.plan"
              ></h3>
              <v-card-text
                class="text-center subtitle-1 white--text py-2"
                v-text="plan.description"
              ></v-card-text>
              <v-card-subtitle
                class="text-h5 font-weight-black text-center white--text pt-0"
                >{{ planDuration === 'monthly' ? plan.monthly : plan.yearly }}
                <span class="subtitle-1"
                  >per {{ planDuration === 'monthly' ? 'month' : 'year' }}</span
                ></v-card-subtitle
              >
              <v-list>
                <v-list-item
                  v-for="(feature, ik) in plan.features"
                  :key="`feature-${ik}`"
                  dense
                >
                  <v-list-item-icon>
                    <v-icon>
                      {{ feature.icon }}
                    </v-icon>
                  </v-list-item-icon>
                  <v-list-item-content>
                    <v-list-item-title
                      class="text-capitalize"
                      v-text="feature.text"
                    ></v-list-item-title>
                  </v-list-item-content>
                </v-list-item>
                <v-list-item>
                  <v-btn
                    color="primary"
                    large
                    block
                    rounded
                    class="mx-auto my-3"
                  >
                    Buy Now
                  </v-btn>
                </v-list-item>
              </v-list>
            </v-card></v-hover
          >
        </v-col>
      </v-row>
    </v-container>
  </section>
</template>

<script>
export default {
  data() {
    return {
      planDuration: 'monthly',
      plans: [
        {
          plan: 'Basic',
          elevation: 0,
          color: 'primary darken-1',
          description: 'Ideal for students, backpackers, and those looking to explore on a budget.',
          monthly: '$10',
          yearly: '$100',
          features: [
            {
              icon: 'mdi-web',
              text: 'Accommodations',
            },
            {
              icon: 'mdi-harddisk',
              text: 'Transportation',
            },
            {
              icon: 'mdi-signal',
              text: 'Essential Sightseeing',
            },
            {
              icon: 'mdi-account',
              text: 'Travel Assistance',
            },
            {
              icon: 'mdi-domain',
              text: 'Group Activities',
            },
            {
              icon: 'mdi-server',
              text: 'Travel Insurance',
            },
            {
              icon: 'mdi-dns',
              text: '24/7 Online Support',
            },
          ],
        },
        {
          plan: 'Silver',
          elevation: 16,
          color: 'green darken-2',
          description: 'Great for families, couples, and solo adventurers',
          monthly: '$40',
          yearly: '$400',
          features: [
            {
              icon: 'mdi-web',
              text: 'Upgraded Accommodations',
            },
            {
              icon: 'mdi-harddisk',
              text: 'Transportation',
            },
            {
              icon: 'mdi-signal',
              text: 'Comprehensive Sightseeing',
            },
            {
              icon: 'mdi-account',
              text: 'Enhanced Travel Assistance',
            },
            {
              icon: 'mdi-domain',
              text: 'Additional Group Activities',
            },
            {
              icon: 'mdi-server',
              text: 'Extended Travel Insurance',
            },
            {
              icon: 'mdi-dns',
              text: 'Local Guides',
            },
          ],
        },
        {
          plan: 'Gold',
          elevation: 0,
          color: 'orange darken-3',
          description: 'Suited for honeymooners, luxury seekers, and anyone desiring a truly bespoke journey.',
          monthly: '$100',
          yearly: '$1000',
          features: [
            {
              icon: 'mdi-web',
              text: 'Luxury Accommodations',
            },
            {
              icon: 'mdi-harddisk',
              text: 'Premium Transportation',
            },
            {
              icon: 'mdi-signal',
              text: 'Exclusive Sightseeing',
            },
            {
              icon: 'mdi-account',
              text: 'Concierge Services',
            },
            {
              icon: 'mdi-domain',
              text: 'Customized Itinerary',
            },
            {
              icon: 'mdi-server',
              text: 'Comprehensive Travel Insurance',
            },
            {
              icon: 'mdi-dns',
              text: 'Private Guides',
            },
          ],
        },
      ],
    }
  },
}
</script>

<style scoped>
.zoom {
  transform: scale(1.025) translate(0, -10px);
  transition: transform 0.2s;
}
.notzoom {
  transition: transform 0.2s;
}
</style>

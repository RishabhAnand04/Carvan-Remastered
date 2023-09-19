<template>
    <section :class="this.$vuetify.theme.dark ? '' : 'grey lighten-4'">
        <v-row no-gutters>
            <v-col cols="12" v-if="secondHeroAlt">
                <SectionsHeroAlt :hero-alt="secondHeroAlt" />
            </v-col>
        </v-row>
        <template>
            <section id="intro" class="py-16">
                <v-container>
                    <v-responsive class="max-auto mx-auto text-center" max-width="600">
                        <v-avatar color="primary" size="70" class="mb-8"> </v-avatar>
                        <h2 class="text-h4 text-md-h3 text-center font-weight-black mb-7">
                            <!-- Unlock Your Journey: Explore, Experience, Evolve -->
                            {{ currentPlaceData.sub_heading }}
                        </h2>
                        <p class="title font-weight-light">
                            {{ currentPlaceData.details }}
                        </p>
                    </v-responsive>

                    <v-row class="pt-12">
                        <v-col v-for="card in cards" :key="card.title" cols="12" md="4">
                            <v-row no-gutters>
                                <v-col :cols="card.callout ? 9 : 12">
                                    <div class="pr-2">
                                        <div class="text--disabled" v-text="card.subtitle"></div>
                                        <h4 class="text-uppercase mt-1 mb-4" style="letter-spacing: 0.15em"
                                            v-text="card.title"></h4>
                                        <p v-text="card.text"></p>
                                    </div>
                                </v-col>
                                <v-col v-if="card.callout" cols="2">
                                    <span class="text-h3 grey--text font-weight-bold pr-8" style="opacity: 0.1">{{
                                        card.callout }}</span>
                                </v-col>
                            </v-row>
                        </v-col>
                    </v-row>
                </v-container>
            </section>
        </template>
        <template>
            <section id="testimonials" :class="$vuetify.theme.dark ? 'black' : 'white'" class="py-16">
                <h2 class="text-h4 text-md-h3 text-center font-weight-black mb-8 my-8">
                    Tour Guides
                </h2>
                <v-carousel cycle draggable="true" hide-delimiter-background hide-delimiters>
                    <v-carousel-item v-for="(item, i) in testimonials" :key="i" class="">
                        <v-container fill-height>
                            <div style="max-width: 700px" class="mx-auto text-center">
                                <v-avatar size="128" class="mb-7">
                                    <img :src="`/team/${item.avtar}`" alt="John" width="128" height="128" />
                                </v-avatar>
                                <h3 :class="$vuetify.theme.dark
                                    ? 'black'
                                    : 'white grey--text text--darken-2'
                                    " class="mb-1 font-weight-black text-uppercase">
                                    {{ item.name }}
                                </h3>
                                <div class="mb-10 font-weight-light grey--text text-uppercase">
                                    {{ item.post }}
                                </div>
                                <v-row>
                                    <v-col cols="1"><v-icon x-large
                                            class="grey--text text--lighten-1">mdi-format-quote-open</v-icon></v-col>
                                    <v-col cols="10">
                                        <div :class="$vuetify.theme.dark
                                            ? 'black'
                                            : 'white grey--text text--darken-2'
                                            " class="mb-5 font-italic">
                                            {{ item.review }}
                                        </div>
                                    </v-col>
                                    <v-col cols="1"><v-icon x-large
                                            class="grey--text text--lighten-1">mdi-format-quote-close</v-icon></v-col>
                                </v-row>
                            </div>
                        </v-container>
                    </v-carousel-item>
                </v-carousel>
            </section>
        </template>
        <iframe
            :src="currentPlaceData.i_frame"
            height="600" width="100%" frameborder="0" style="border: 0; display: block" allowfullscreen="true"
            aria-hidden="false" tabindex="0"></iframe>

    </section>
</template>

<script>
export default {
    data() {
        return {
            cards: [
                {
                    title: "Interactive Virtual Tours",
                    subtitle: "Professionally developed",
                    text: "All components and features are developed using the most up-to-date coding practices.",
                    callout: "01",
                },
                {
                    title: "Fast & optimized",
                    subtitle: "Performance",
                    text: "Themes are designed for maximum performance and are semantically structured to maximize SEO.",
                    callout: "02",
                },
                {
                    title: "Built on Vuetify",
                    subtitle: "Material Design",
                    text: "Being developed with Vuetify means you have access to all of the framework's available features.",
                    callout: "03",
                },
            ],
            testimonials: [
                {
                    avtar: 'person-4.jpg',
                    name: 'Olivia Anderson',
                    post: 'Experienced Tour Guide',
                    review: "Olivia is an amazing tour guide! Her in-depth knowledge of the local history and culture made our trip unforgettable. She took us on a journey through the hidden gems of the region, and her storytelling skills kept us engaged throughout the tour."
                },
                {
                    avtar: 'person-8.jpg',
                    name: 'Maxwell Davis',
                    post: 'Adventure Tour Specialist',
                    review: "Maxwell is a true adventure enthusiast. He led us on adrenaline-pumping expeditions, from challenging treks to thrilling water sports. His passion for the outdoors is infectious, and he made every moment of our adventure tour memorable."
                },
                {
                    avtar: 'person-7.jpg',
                    name: 'Isabella Martinez',
                    post: 'Cultural Heritage Guide',
                    review: "Isabella is a treasure trove of cultural insights. She introduced us to the rich traditions and customs of the region, and her guided tours of local landmarks left us with a deeper appreciation for the heritage. Her warmth and enthusiasm were truly inspiring."
                },
                {
                    avtar: 'person-10.jpg',
                    name: 'Ethan Johnson',
                    post: 'Nature Explorer Guide',
                    review: "Ethan is a nature enthusiast like no other. His knowledge of flora and fauna is astounding, and he led us on serene nature escapes that allowed us to reconnect with the natural world. If you're seeking tranquility and awe-inspiring landscapes, Ethan is the guide to choose."
                }
            ],
            secondHeroAlt: [],
            currentPlaceData: {},
        };
    },
    mounted() {
        const dataQueryParam = this.$route.query.data;
        if (dataQueryParam) {
            // Parse the JSON string into an object
            const selectedTouristPlace = JSON.parse(dataQueryParam);
            this.currentPlaceData = selectedTouristPlace;
            this.currentPlaceData = {
                ...selectedTouristPlace,
                heading: selectedTouristPlace.name,
                src: "pexels-andrea-piacquadio-3884440.jpg",
            };
            this.secondHeroAlt = [
                {
                    src: this.currentPlaceData.image_str,
                    heading: this.currentPlaceData.heading,
                    subHeading: this.currentPlaceData.location,
                    description: this.currentPlaceData.description,
                },
            ];
        }
    },
    head() {
        return {
            title: "Blog",
            meta: [
                {
                    hid: "description",
                    name: "description",
                    content:
                        "Infographic hypotheses influencer user experience Long madel ture gen-z paradigm shift client partner network product seilans solve management influencer analytics leverage virality. incubator seed round massmarket. buyer agile development growth hacking business-to-consumer ecosystem",
                },
            ],
        };
    },
};
</script>

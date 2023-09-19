<template>
    <section>
        <v-skeleton-loader color="secondary" type="card-avatar" v-if="!cityData"></v-skeleton-loader>
        <v-row no-gutters v-if="cityData">
            <v-col cols="12">
                <!-- <SectionsHeroAlt :hero-alt="heroAlt" /> -->
                <v-container>
                    <v-row class="py-16">
                        <v-col cols="12">
                            <h2 class="text-h4 text-md-h3 text-center font-weight-black text-capitalize">
                                Tourist Places to Visit in {{ currentCityObj.name }}
                            </h2>
                        </v-col>
                    </v-row>
                </v-container>
                <v-row no-gutters v-for="(place, index) in cityData" :key="place.id"
                    :class="{ 'flex-row-reverse': index % 2 === 1 }">
                    <v-col cols="12" md="6" align-self="center">
                        <v-hover  v-slot="{ hover }">
                            <v-card @click="redirectToIndividualPage(place.name)" :elevation="hover ? 24 : 16" 
                                :class="hover ? 'zoom' : 'notzoom'" class="mx-auto transition-swing">
                                <v-img max-height="500" :src="place.image_str" :lazy-src="place.image_str">
                                </v-img>
                            </v-card></v-hover>
                    </v-col>
                    <v-col cols="12" md="6" align-self="center">
                        <div class="px-8 py-2">
                            <h2 @click="redirectToIndividualPage(place.name)" class="text-h3 text-center font-weight-black"
                                :class="dynamicH2Class(index)">{{
                                    place.name
                                }}</h2>
                            <h3 class="text-h5 text-uppercase font-weight-thin text-center my-8"
                                :class="dynamicH3Class(index)">
                                {{ place.location }}
                            </h3>
                            <p>
                                {{ place.description }}
                            </p>
                            <div :class="dynamicH2Class(index)"><strong>Rating -
                                    {{ place.rating }}
                                </strong>
                            </div>
                        </div>
                    </v-col>
                </v-row>

            </v-col>
        </v-row>
    </section>
</template>

<script>
export default {
    props: {
        cityData: Array,
        currentCityObj: Object,
    },
    data() {
        return {
            heroAlt: [
                {
                    src: "pexels-moose-photos-1036641.jpg",
                    heading: " Chandigarh ",
                    subHeading: "The most affordable pricing",
                    description: "lorem about",
                },
            ],
            ourTeam: [
                {
                    name: "John Churchill",
                    position: "Marketing Director",
                    phone: "+1 (987) 1625346",
                    email: "john@example.com",
                    photo: "person-1.jpg",
                },
                {
                    name: "Fiona	Ross",
                    position: "Project Manager",
                    phone: "+1 (987) 5894684",
                    email: "fiona@example.com",
                    photo: "person-2.jpg",
                },
                {
                    name: "Justin	Rees",
                    position: "VP Marketing",
                    phone: "+1 (987) 6982456",
                    email: "justin@example.com",
                    photo: "person-3.jpg",
                },
                {
                    name: "Amelia	Ogden",
                    position: "Communication Manager",
                    phone: "+1 (987) 6982456",
                    email: "amelia@example.com",
                    photo: "person-4.jpg",
                },
                {
                    name: "Sebastian Bailey",
                    position: "Advertising Director",
                    phone: "+1 (987) 6982456",
                    email: "sebastian@example.com",
                    photo: "person-5.jpg",
                },
                {
                    name: "Eric Sutton",
                    position: "Advertising Executive",
                    phone: "+1 (987) 6982456",
                    email: "audrey@example.com",
                    photo: "person-6.jpg",
                },
                {
                    name: "Xia Yen",
                    position: "Advertising Manager",
                    phone: "+1 (987) 6982456",
                    email: "christian@example.com",
                    photo: "person-7.jpg",
                },
                {
                    name: "Bernadette	Springer",
                    position: "Employee Relations Manager",
                    phone: "+1 (987) 6982456",
                    email: "bernadette@example.com",
                    photo: "person-8.jpg",
                },
                {
                    name: "Elizabeth Newman",
                    position: "Project Manager",
                    phone: "+1 (987) 6982456",
                    email: "elizabeth@example.com",
                    photo: "person-9.jpg",
                },
            ],
        };
    },
    methods: {
        redirectToIndividualPage(placeName) {
            this.$router.push('/tourist-place');
            const selectedTouristPlace = this.cityData.find(place => place.name === placeName);
            this.$router.push({ path: '/tourist-place', query: { data: JSON.stringify(selectedTouristPlace) } });
        },
        dynamicH2Class(index) {
            const colors = ['color-class-1', 'color-class-2', 'color-class-3', 'color-class-4'];
            const colorIndex = index % colors.length;
            return colors[colorIndex];
        },
        dynamicH3Class(index) {
            const colors = ['color-class-3', 'color-class-4', 'color-class-1', 'color-class-2'];
            const colorIndex = index % colors.length;
            return colors[colorIndex];
        },
    },

    head() {
        return {
            title: this.currentCityObj.name,
        };
    },
};
</script>
<style lang="scss" scoped>
.color-class-1 {
    color: brown;
}

.color-class-2 {
    color: rgb(65, 144, 28);
}

.color-class-3 {
    color: rgb(11, 26, 238);
}

.color-class-4 {
    color: rgb(220, 150, 46);
}
.zoom {
  transform: scale(1.025) translate(0, -10px);
  transition: transform 0.2s;
}
.notzoom {
  transition: transform 0.2s;
}
</style>

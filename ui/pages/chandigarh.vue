<template>
    <div>
        <SectionsCity :city-data="cityData" :city-name="Chandigarh"></SectionsCity>
    </div>
</template>

<script>
export default {
    data() {
        return {
            cityData: null,
            currentCityData: {}, 
        };
    },
    mounted() {
        this.getPlaces();
        this.getCityData();
    },
    methods: {
        async getPlaces() {
            try {
                const response = await fetch('http://127.0.0.1:8000/api/Places');
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                const data = await response.json();
                this.currentCityData = data;
            } catch (error) {
                console.error('Error fetching places:', error);
            }
        },
        async getCityData() {
            try {
                const response = await fetch(`http://127.0.0.1:8000/api/Visiting`);
                if (!response.ok) {
                    throw new Error("Network response was not ok");
                }
                const data = await response.json();
                this.cityData = data;
            } catch (error) {
                console.error("Error fetching places:", error);
            }
        },
    },
};
</script>

<style></style>
<template>
  <div>
    <h1>Your IP is: {{ ip }}</h1>
    <h2>Your Location is: {{ location }}</h2>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'Ip',
  data() {
    return {
      ip: '',
      location: '',
    };
  },
  methods: {
    async getIpAndLocation() {
      const path = '/api/ip';
      try {
        const res = await axios.get(path);
        this.ip = res.data.ip;
        this.location = res.data.city;
      }
      catch (error) {
        console.error(error);
      }
    },
  },
  created() {
    this.getIpAndLocation();
  },
};
</script>

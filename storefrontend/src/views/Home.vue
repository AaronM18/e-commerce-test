<template>
  <div class="home">
    <section class="hero is-medium is-dark mb-6">
      <div class="hero-body has-text-centered">
        <p class="title mb-6">
          Welcome to Store
        </p>
        <p class="subtitle">
          The best jacket store online
        </p>
      </div>
    </section>
    <div class="columns is-multiline">
      <div class="column is-12">
        <h2 class="is-size-2 has-text-centered">Latest Products</h2>
      </div>
      <ProductBox
        v-for="product in latestProducts"
        v-bind:key="product.id"  
        v-bind:product="product"
      />
    </div>
  </div>
</template>

<script>
import axios from 'axios';

import ProductBox from '../components/ProductsBox';

export default {
  name: 'Home',
  data() {
    return {
      latestProducts:  [],
    }
  },
  components: {
    ProductBox,
  },
  mounted() {
    this.getLatestProducts()
    document.title = 'Home | Store';
  },
  methods: {
    getLatestProducts() {
      axios.get('/api/v1/latest-products/')
      .then(res => {
        this.latestProducts = res.data
      })
      .catch(e => {
        console.error(e);
      });
    }
  },
}
</script>


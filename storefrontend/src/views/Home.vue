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
      <div
        class="column is-3"
        v-for="product in latestProducts"
        v-bind:key="product.id"  
      >
        <div class="box">
          <figure class="image mb-4">
            <img class="product-image" v-bind:src="product.get_thumbnail"/>
          </figure>
          <h3 class="is-size-4">{{ product.name }}</h3>
          <p class="is-size-6 has-text-gray">${{ product.price }}</p>
          
          <router-link v-bind:to="product.get_absolute_url" class="button is-dark -mt-4">View Details</router-link>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Home',
  data() {
    return {
      latestProducts:  [],
    }
  },
  components: {
    
  },
  mounted() {
    this.getlatestProducts()
    document.title = 'Home | Store';
  },
  methods: {
    getlatestProducts() {
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

<style scoped>
  .image {
    margin-top: -1.25rem;
    margin-left: -1.25rem;
    margin-right: -1.25rem;
  }
  .product-image {
    max-height: 180px;
    width: auto;
    margin: 0 auto;
  }
</style>
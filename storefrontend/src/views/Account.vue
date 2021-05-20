<template>
	<div class="page-account">
		<div class="columns is-multiline">
			<div class="column is-12">
				<h1 class="title">Account</h1>
			</div>
			<div class="column is-12">
				<button @click="signOut()" class="button is-danger">
					Sign out
				</button>
			</div>
			<hr>
			<div class="column is-12">
				<h2 class="subtitle">My Orders</h2>
			</div>
			<div class="column is-12">
				<OrderSummary
					v-for="order in orders"
					v-bind:key="order.id"
					v-bind:order="order"
				/>
			</div>
		</div>
	</div>
</template>

<script>
import axios from 'axios';
import OrderSummary from '../components/OrderSummary.vue';
export default {
	name: 'Account',
	components: {
		OrderSummary,
	},
	data() {
		return {
			orders: [],
		}
	},
	mounted() {
		document.title = 'Account | Store';
		this.getMyOrders();
	},
	methods: {
		signOut() {
			axios.defaults.headers.common['Authorization'] = '';
			
			localStorage.removeItem('token');
			localStorage.removeItem('username');
			localStorage.removeItem('userid');

			this.$store.commit('removeToken');
			this.$router.push('/');
		},
		async getMyOrders() {
			this.$store.commit('setIsLoading', true);

			await axios.get('/api/v1/orders/').then(response => {
				this.orders = response.data;
			}).catch(error => {
				console.error(error);
			});

			this.$store.commit('setIsLoading', false);
		}
	},
}
</script>
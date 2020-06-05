import Vue from 'https://cdn.jsdelivr.net/npm/vue@latest/dist/vue.esm.browser.min.js';
//import axios from 'https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js';

new Vue({
	delimiters: ['${', '}'],
  	el: '#app',
  	data: {
  		inputText: '',
  	},
  	methods: {
  		cleanInput() {
  			this.inputText = '';
  		}
  	},
  	computed: {
  		realMoney() {
  			return `R$ ${this.inputText}`;
  		}
  	}
});
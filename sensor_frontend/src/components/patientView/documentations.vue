<template>
  <div class="bg-gray-200 text-slate-900 rounded-xl mr-5 min-w-max min-h-screen">

      <div>
          {{documentation}}
      </div>
  </div>
</template>
<script>



import axios from "axios";

export default {
    data() {
        return {
            documentation: ''
        }
    },
    methods: {
        async documentsList() {
            await axios
                .get('/api/documentation/list')
                .then(
                    response => {
                        this.documentation = response.data
            }
                )
        }
    },
    mounted() {
        this.documentsList()
    }
}


</script>
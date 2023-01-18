<template>
  <div class="container mt-3">
    <div class="row">
      <div class="col">
        <p class="h3 text-success fw-bold">Edit Contact</p>
        <p class="fst-italic">Lorem ipsum dolor, sit amet consectetur adipisicing elit. Sequi doloremque sed cumque consequatur repellat facilis ex reiciendis qui, similique dolorem enim quisquam, quod nobis, tempora aut? Corrupti tempore esse sit.</p>
      </div>
    </div>
  </div>
  <div class="container mt-3">
    <div class="row">
      <div class="col-md-4">
        <form @submit.prevent="submitUpdate()">
          <div class="mb-2">
            <input v-model="contact.name" type="text" class="form-control" placeholder="Name">
          </div>
          <div class="mb-2">
            <input v-model="contact.photo" type="text" class="form-control" placeholder="Photo URL">
          </div>
          <div class="mb-2">
            <input v-model="contact.email" type="text" class="form-control" placeholder="Email">
          </div>
          <div class="mb-2">
            <input v-model="contact.mobile" type="number" class="form-control" placeholder="Mobile">
          </div>
          <div class="mb-2">
            <input v-model="contact.company" type="text" class="form-control" placeholder="Company">
          </div>
          <div class="mb-2">
            <input v-model="contact.title" type="text" class="form-control" placeholder="Title">
          </div>
          <div class="mb-2">
            <select v-model="contact.groupId" class="form-control" v-if="groups.length > 0">
              <option value="">Select Group</option>
              <option :value="group.id" v-for="group of groups" :key="group.id">{{group.name}}</option>
            </select>
          </div>
          <div class="mb-2">
            <input type="submit" class="btn btn-danger" value="Update">
            <router-link to="/" class="btn btn-dark ms-2">close</router-link>
          </div>
        </form>
      </div>
      <div class="col-md-4">
        <img :src="contact.photo" alt="" class="contact-img">
      </div>
    </div>
  </div>
</template>
  
<script>
import { ContactService } from '@/services/ContactService';

    export default {
      name: 'EditContact',
      data : function (){
        return {
          contact : {
            name : '',
            photo : '',
            email : '',
            company : '',
            title : '',
            groupId : '',
          },
          contactId : this.$route.params.contactId,
          loading : false,
          errorMessage : null,
          groups : []
        }
      },
      created : async function (){
        try {
          this.loading = true;
          let response = await ContactService.getContact(this.contactId);
          let groupResponse = await ContactService.getAllGroups();
          this.groups = groupResponse.data;
          this.contact = response.data;
          this.loading = false;
        } catch (error) {
          this;this.errorMessage = error;
          this.loading = false;
        }
      },
      methods : {
        submitUpdate : async function (){
          try {
            let response = await ContactService.updateContact(this.contact, this.contactId);
            if(response){
              return this.$router.push('/');
            }
            else{
              return this.$router.push(`/contacts/edit/${this.contactId}`);
            }
          } catch (error) {
              console.log(error);
          }
        }
      }
    }
</script>

<style scoped>
    
</style>
  
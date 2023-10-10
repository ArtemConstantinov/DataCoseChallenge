<template>
    <b-card
        style="max-width: 20rem; width: 100%;"
        title="Sign In"
        bg-variant="dark" 
        text-variant="white"
    >
        <b-form @submit.prevent="userLogin">
            <b-form-group id="input-group-1" label="Username:" label-for="input-1">
                <b-form-input
                    id="input-1"
                    v-model="login.username"
                    placeholder="Enter username"
                    required
                />
            </b-form-group>
            <b-form-group id="input-group-2" label="Password:" label-for="input-2">
                <b-form-input
                    id="input-2"
                    v-model="login.password"
                    placeholder="Enter password"
                    type="password"
                    required
                />
            </b-form-group>
            <div class="actions-container">
                <b-button type="submit" variant="primary">
                    <span class="mdi mdi-login" style="margin-right: 0.4rem;"></span>
                    Submit
                </b-button>
            </div>
        </b-form>
    </b-card>
</template>

<script>

export default {
    layout: "initial",
    middleware: "auth",
    auth: "guest",
    
    data() {
        return {
            login: {
                username: "admin",
                password: "guest"
            }
        }
    },
    methods: {
        async userLogin() {
            try {
                const response = await this.$auth.loginWith(
                    "local", 
                    {data: this.login}
                );
                this.$nuxt.$router.push("/");
                console.log(response);
            } catch (err) {
                console.log(err)
            }
        }
    }
}
</script>

<style lang="scss" scoped>
.actions-container
{
    display: grid;
    justify-items: end;
    margin-top: 2.5rem;
}
</style>
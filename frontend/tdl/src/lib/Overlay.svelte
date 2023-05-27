<script>
    import SupabaseSignin from "./SupabaseSignin.svelte";

    import { createClient } from '@supabase/supabase-js'

    const supabase = createClient('https://wzlxhmothxekqaejfgie.supabase.co', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Ind6bHhobW90aHhla3FhZWpmZ2llIiwicm9sZSI6ImFub24iLCJpYXQiOjE2ODE4NzI2MTEsImV4cCI6MTk5NzQ0ODYxMX0.AXuwk18Bhc8C09k7V4Dmx-VBkvIEKYqkHjJLOUbfgU0')

    let isOpen = false
    let isSignined = false
    
    let email = null
    let password = null

    async function SignUp () {
        const { data, error } = await supabase.auth.signUp({
        email: email,
        password: password,
        })
    }

    async function SignIn () {
        const { data, error } = await supabase.auth.signInWithPassword({
        email: email,
        password: password,
        })
    }
</script>

<button class="" on:click={() => {isOpen = isOpen ? false : true}}>Overlay</button>

{#if isOpen}
    <div class="w-80 h-screen absolute top-12 right-2">
        <div class=" grid border-dashed rounded-2xl w-80 border-4 p-2 shadow-xl text-black">
            <input class="m-2 p-1 rounded-md" type="email" bind:value={email} placeholder="email">
            <input class="m-2 p-1 rounded-md" type="password" bind:value={password} placeholder="password">
            <button on:click={SignIn} class="m-2 p-1 rounded-md bg-blue-400 hover:bg-blue-500">Sign In</button>
            <button on:click={SignUp} class="m-2 p-1 rounded-md bg-blue-400 hover:bg-blue-500">Sign Up</button>
            <!-- <SupabaseSignin></SupabaseSignin> -->
        </div>
    </div>
{/if}

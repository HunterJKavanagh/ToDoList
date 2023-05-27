<script>
    import { createClient } from '@supabase/supabase-js'
    import Auth from 'supabase-ui-svelte'

    const supabaseClient = createClient('https://wzlxhmothxekqaejfgie.supabase.co', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Ind6bHhobW90aHhla3FhZWpmZ2llIiwicm9sZSI6ImFub24iLCJpYXQiOjE2ODE4NzI2MTEsImV4cCI6MTk5NzQ0ODYxMX0.AXuwk18Bhc8C09k7V4Dmx-VBkvIEKYqkHjJLOUbfgU0')

</script>

<Auth {supabaseClient}/>
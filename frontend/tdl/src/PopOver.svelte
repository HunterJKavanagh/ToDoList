<script>
    import { fade, scale } from 'svelte/transition';
    import { quintOut } from 'svelte/easing';

    let visible = false;
</script>


<button on:click={() => (visible = true)}>Open</button>

{#if visible}
    <!-- svelte-ignore a11y-click-events-have-key-events -->
    <div transition:fade on:click|stopPropagation>
        <div on:click|stopPropagation={() => (visible = false)} transition:scale={{ delay: 25, duration: 150, easing: quintOut }}>
            Backdrop
        </div>
        <div>Content</div>
    </div>
{/if}


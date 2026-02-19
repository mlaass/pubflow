<script lang="ts">
	import favicon from '$lib/assets/favicon.svg';
	import '../app.css';

	let { children } = $props();
</script>

<svelte:head>
	<link rel="icon" href={favicon} />
</svelte:head>

<div class="min-h-screen bg-background font-sans antialiased">
	<header class="border-b border-border">
		<div class="mx-auto flex h-14 max-w-3xl items-center px-6">
			<a href="/" class="text-lg font-semibold tracking-tight">PubFlow</a>
			<nav class="ml-auto flex gap-4 text-sm text-muted-foreground">
				<a href="/blog" class="transition-colors hover:text-foreground">Blog</a>
			</nav>
		</div>
	</header>
	<main class="mx-auto max-w-3xl px-6 py-10">
		{@render children()}
	</main>
</div>

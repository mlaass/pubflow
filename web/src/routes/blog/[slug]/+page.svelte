<script lang="ts">
	import type { Post } from '$lib/types';
	import type { Component } from 'svelte';

	let { data } = $props();
	const content: Component = data.content;
	const meta: Post = data.meta;
</script>

<article>
	<a
		href="/blog"
		class="mb-8 inline-flex items-center text-sm text-muted-foreground transition-colors hover:text-foreground"
	>
		&larr; Back to blog
	</a>

	<header class="mb-8 border-b border-border pb-6">
		<h1 class="text-3xl font-bold tracking-tight sm:text-4xl">{meta.title}</h1>
		<div class="mt-3 flex items-center gap-3 text-sm text-muted-foreground">
			<time datetime={meta.created}>{meta.created}</time>
			{#if meta.tags?.length > 0}
				<span class="text-border">|</span>
				<span>{meta.tags.join(', ')}</span>
			{/if}
		</div>
	</header>

	<div class="prose">
		<svelte:component this={content} />
	</div>
</article>

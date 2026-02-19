<script lang="ts">
	import type { Post } from '$lib/types';

	let { data } = $props();
	const posts: Post[] = data.posts;
</script>

<div class="space-y-8">
	<h1 class="text-3xl font-bold tracking-tight">Blog</h1>

	{#if posts.length === 0}
		<div class="rounded-lg border border-dashed border-border p-8 text-center">
			<p class="text-muted-foreground">
				No posts yet. Use <code class="rounded bg-muted px-1.5 py-0.5 font-mono text-sm">/pub.new</code> to create your first article.
			</p>
		</div>
	{:else}
		<div class="grid gap-4">
			{#each posts as post}
				<a
					href="/blog/{post.slug}"
					class="group rounded-lg border border-border bg-card p-5 transition-colors hover:bg-accent"
				>
					<h2 class="font-semibold tracking-tight group-hover:text-accent-foreground">
						{post.title}
					</h2>
					<div class="mt-2 flex items-center gap-3 text-sm text-muted-foreground">
						<time datetime={post.created}>{post.created}</time>
						{#if post.tags.length > 0}
							<span class="text-border">|</span>
							<span>{post.tags.join(', ')}</span>
						{/if}
					</div>
				</a>
			{/each}
		</div>
	{/if}
</div>

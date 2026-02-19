import type { Post } from '$lib/types';
import { error } from '@sveltejs/kit';

export async function load({ params }) {
	try {
		const post = await import(`../../../lib/content/${params.slug}.md`);
		return {
			content: post.default,
			meta: post.metadata as Post
		};
	} catch {
		error(404, `Post not found: ${params.slug}`);
	}
}

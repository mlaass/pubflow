import type { Post } from '$lib/types';

export async function load() {
	const modules = import.meta.glob<{
		metadata: Post;
	}>('$lib/content/*.md', { eager: true });

	const posts: Post[] = Object.entries(modules).map(([path, mod]) => {
		const slug = path.split('/').pop()!.replace('.md', '');
		return { ...mod.metadata, slug };
	});

	posts.sort((a, b) => new Date(b.created).getTime() - new Date(a.created).getTime());

	return { posts };
}

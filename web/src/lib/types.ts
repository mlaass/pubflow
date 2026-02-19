export interface Post {
	slug: string;
	title: string;
	id: string;
	created: string;
	tags: string[];
	stage: string;
	heroImage?: string;
	heroAlt?: string;
	excerpt?: string;
}

import { type ClassValue, clsx } from "clsx";
import { twMerge } from "tailwind-merge";

export function cn(...inputs: ClassValue[]) {
	return twMerge(clsx(inputs));
}

import type { Snippet } from "svelte";

// shadcn-svelte type helpers
type Primitive<T> = T & { class?: string | null | undefined };

type WithoutChildrenOrChild<T> = T extends infer U
	? Omit<U, "children" | "child">
	: never;

export type WithoutChild<T> = T extends infer U ? Omit<U, "child"> : never;

export type WithoutChildren<T> = T extends infer U
	? Omit<U, "children">
	: never;

export type WithElementRef<T, El extends HTMLElement = HTMLElement> = T & {
	ref?: El | null;
};

export type { Primitive, WithoutChildrenOrChild };

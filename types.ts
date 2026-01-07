// types.ts
export interface User {
  id: string;
  name: string;
  email: string;
}

export interface Product {
  id: number;
  name: string;
  price: number;
  description: string;
}

export interface CartItem {
  product: Product;
  quantity: number;
}

export interface Cart {
  items: CartItem[];
  total: number;
}

export enum StatusCode {
  SUCCESS = 200,
  NOT_FOUND = 404,
  INTERNAL_SERVER_ERROR = 500,
}

export interface ApiResponse<T> {
  status: StatusCode;
  data: T | null;
  error: string | null;
}
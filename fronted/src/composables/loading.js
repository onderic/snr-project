import { ref, provide, inject } from 'vue'

const loadingKey = Symbol('loading')

export function provideLoading() {
  const loading = ref(false)
  provide(loadingKey, loading)
  return loading
}

export function useLoading() {
  const loading = inject(loadingKey)
  if (!loading) {
    throw new Error('useLoading must be used within a provideLoading context')
  }
  return loading
}
import { ref, watch } from 'vue'

export function refMinDelay(
  sourceRef,
  delay,
  conditionToDoSomethingImmediate = newValue => newValue === true,
  doImmediate = newValue => newValue,
  doAfterDelay = newValue => newValue,
) {
  let timeId = null
  const delayRef = ref(sourceRef.value)

  watch(sourceRef, () => {
    if (conditionToDoSomethingImmediate(sourceRef.value)) {
      clearTimeout(timeId)
      delayRef.value = doImmediate(sourceRef.value)

      timeId = setTimeout(() => {
        timeId = null
        if (conditionToDoSomethingImmediate(sourceRef.value)) return
        delayRef.value = doAfterDelay(sourceRef.value)
      }, delay)
    } else {
      if (timeId) return
      delayRef.value = doAfterDelay(sourceRef.value)
    }
  }, {
    immediate: true,
  })

  return delayRef
}

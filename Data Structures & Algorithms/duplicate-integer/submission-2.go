func hasDuplicate(nums []int) bool {
    hashMap := make(map[int]bool)

    for _, value := range nums{
        if hashMap[value]{
            return true
            }
        hashMap[value] = true
        } 
    return false
}

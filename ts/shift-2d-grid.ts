function shiftGrid(grid: number[][], k: number): number[][] {
    const [R, C] = [grid.length, grid[0].length]
    k %= R * C
    const res: number[][] = Array.from({ length: R }, x => Array.from({ length: C }))

    for (let r = 0; r < R; r++) {
        for (let c = 0; c < C; c++) {
            res[(r + Math.floor((c + k) / C)) % R][(c + k) % C] = grid[r][c]
        }
    }
    return res
};
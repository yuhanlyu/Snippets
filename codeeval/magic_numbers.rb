File.open(ARGV[0]).each_line do |line|
    a, b = line.split.map(&:to_i)
    result = (a..b).each_with_object([]) {|x, t|
        x = x.to_s.split("")
        next if x.uniq.size != x.size
        visited, cur = [false] * x.size, 0
        begin 
            cur = (cur + x[cur].to_i) % x.size
            break if visited[cur]
            visited[cur] = true
        end until cur == 0
        t << x.join if cur == 0 and visited.all? {|x| x == true}
    }
    puts result.size > 0 ? result.join(" ") : -1
end

File.open(ARGV[0]).each_line do |line|
    edge = line.split(" | ").each_with_object(Hash.new {|h, k| h[k]=[]}) {|x, h|
        h[x[0]] << x[1]
    }.each {|h, k| k.sort!}
    f = lambda {|root|
        root + " [" + edge[root].each_with_object([]) {|child, result|
            if edge.has_key?(child)
                result << f.call(child)
            else
                result << child
            end
        }.join(", ") + "]"
    }
    puts f.call("a")
end

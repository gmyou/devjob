devjob
======

Collection Log

	/usr/local/redis-stable/src/redis-server


	screen -S ElasticSearch
	sh-3.2# j/usr/local/opt/elasticsearch/bin/elasticsearch -f

	        at org.elasticsearch.common.netty.handler.codec.frame.FrameDecoder.cleanup(FrameDecoder.java:482)
	        at org.elasticsearch.common.netty.handler.codec.frame.FrameDecoder.channelDisconnected(FrameDecoder.java:365)
	        at org.elasticsearch.common.netty.channel.SimpleChannelUpstreamHandler.handleUpstream(SimpleChannelUpstreamHandler.java:102)
	        at org.elasticsearch.common.netty.channel.DefaultChannelPipeline.sendUpstream(DefaultChannelPipeline.java:564)
	        at org.elasticsearch.common.netty.channel.DefaultChannelPipeline$DefaultChannelHandlerContext.sendUpstream(DefaultChannelPipeline.java:791)
	        at org.elasticsearch.common.netty.OpenChannelsHandler.handleUpstream(OpenChannelsHandler.java:74)
	        at org.elasticsearch.common.netty.channel.DefaultChannelPipeline.sendUpstream(DefaultChannelPipeline.java:564)
	        at org.elasticsearch.common.netty.channel.DefaultChannelPipeline.sendUpstream(DefaultChannelPipeline.java:559)
	        at org.elasticsearch.common.netty.channel.Channels.fireChannelDisconnected(Channels.java:396)
	        at org.elasticsearch.common.netty.channel.socket.nio.AbstractNioWorker.close(AbstractNioWorker.java:360)
	        at org.elasticsearch.common.netty.channel.socket.nio.NioServerSocketPipelineSink.handleAcceptedSocket(NioServerSocketPipelineSink.java:81)
	        at org.elasticsearch.common.netty.channel.socket.nio.NioServerSocketPipelineSink.eventSunk(NioServerSocketPipelineSink.java:36)
	        at org.elasticsearch.common.netty.channel.DefaultChannelPipeline.sendDownstream(DefaultChannelPipeline.java:574)
	        at org.elasticsearch.common.netty.channel.Channels.close(Channels.java:812)
	        at org.elasticsearch.common.netty.channel.AbstractChannel.close(AbstractChannel.java:197)
	        at org.elasticsearch.transport.netty.NettyTransport.exceptionCaught(NettyTransport.java:523)
	        at org.elasticsearch.transport.netty.MessageChannelHandler.exceptionCaught(MessageChannelHandler.java:229)
	        at org.elasticsearch.common.netty.channel.SimpleChannelUpstreamHandler.handleUpstream(SimpleChannelUpstreamHandler.java:112)
	        at org.elasticsearch.common.netty.channel.DefaultChannelPipeline.sendUpstream(DefaultChannelPipeline.java:564)
	        at org.elasticsearch.common.netty.channel.DefaultChannelPipeline$DefaultChannelHandlerContext.sendUpstream(DefaultChannelPipeline.java:791)
	        at org.elasticsearch.common.netty.handler.codec.frame.FrameDecoder.exceptionCaught(FrameDecoder.java:377)
	        at org.elasticsearch.common.netty.channel.SimpleChannelUpstreamHandler.handleUpstream(SimpleChannelUpstreamHandler.java:112)
	        at org.elasticsearch.common.netty.channel.DefaultChannelPipeline.sendUpstream(DefaultChannelPipeline.java:564)
	        at org.elasticsearch.common.netty.channel.DefaultChannelPipeline$DefaultChannelHandlerContext.sendUpstream(DefaultChannelPipeline.java:791)
	        at org.elasticsearch.common.netty.OpenChannelsHandler.handleUpstream(OpenChannelsHandler.java:74)
	        at org.elasticsearch.common.netty.channel.DefaultChannelPipeline.sendUpstream(DefaultChannelPipeline.java:564)
	        at org.elasticsearch.common.netty.channel.DefaultChannelPipeline.sendUpstream(DefaultChannelPipeline.java:559)
	        at org.elasticsearch.common.netty.channel.Channels.fireExceptionCaught(Channels.java:525)
	        at org.elasticsearch.common.netty.channel.AbstractChannelSink.exceptionCaught(AbstractChannelSink.java:48)
	        at org.elasticsearch.common.netty.channel.DefaultChannelPipeline.notifyHandlerException(DefaultChannelPipeline.java:658)
	        at org.elasticsearch.common.netty.channel.DefaultChannelPipeline.sendUpstream(DefaultChannelPipeline.java:566)
	        at org.elasticsearch.common.netty.channel.DefaultChannelPipeline$DefaultChannelHandlerContext.sendUpstream(DefaultChannelPipeline.java:791)
	        at org.elasticsearch.common.netty.OpenChannelsHandler.handleUpstream(OpenChannelsHandler.java:74)
	        at org.elasticsearch.common.netty.channel.DefaultChannelPipeline.sendUpstream(DefaultChannelPipeline.java:564)
	        at org.elasticsearch.common.netty.channel.DefaultChannelPipeline.sendUpstream(DefaultChannelPipeline.java:559)
	        at org.elasticsearch.common.netty.channel.Channels.fireMessageReceived(Channels.java:268)
	        at org.elasticsearch.common.netty.channel.Channels.fireMessageReceived(Channels.java:255)
	        at org.elasticsearch.common.netty.channel.socket.nio.NioWorker.read(NioWorker.java:88)
	        at org.elasticsearch.common.netty.channel.socket.nio.AbstractNioWorker.process(AbstractNioWorker.java:108)
	        at org.elasticsearch.common.netty.channel.socket.nio.AbstractNioSelector.run(AbstractNioSelector.java:318)
	        at org.elasticsearch.common.netty.channel.socket.nio.AbstractNioWorker.run(AbstractNioWorker.java:89)
	        at org.elasticsearch.common.netty.channel.socket.nio.NioWorker.run(NioWorker.java:178)
	        at org.elasticsearch.common.netty.util.ThreadRenamingRunnable.run(ThreadRenamingRunnable.java:108)
	        at org.elasticsearch.common.netty.util.internal.DeadLockProofWorker$1.run(DeadLockProofWorker.java:42)
	        at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1145)
	        at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:615)
	        at java.lang.Thread.run(Thread.java:744)

	screen -S logstash-shipper
	sh-3.2# java -jar /usr/local/opt/logstash/libexec/logstash-1.3.3-flatjar.jar agent -f /usr/local/opt/logstash/logstash-shipper.conf


			You are using a deprecated config setting "format" set in file. Deprecated settings will continue to work, but are scheduled for removal from logstash in the future. You should use the newer 'codec' setting instead. If you have any questions about this, please visit the #logstash channel on freenode irc. {:name=>"format", :plugin=><LogStash::Inputs::File --->, :level=>:warn}
			Using milestone 2 input plugin 'file'. This plugin should be stable, but if you see strange behavior, please let us know! For more information on plugin milestones, see http://logstash.net/docs/1.3.3/plugin-milestones {:level=>:warn}
			Using milestone 2 codec plugin 'oldlogstashjson'. This plugin should be stable, but if you see strange behavior, please let us know! For more information on plugin milestones, see http://logstash.net/docs/1.3.3/plugin-milestones {:level=>:warn}
			Using milestone 2 output plugin 'redis'. This plugin should be stable, but if you see strange behavior, please let us know! For more information on plugin milestones, see http://logstash.net/docs/1.3.3/plugin-milestones {:level=>:warn}

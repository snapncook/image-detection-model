.SILENT:

.bin-deps:
	$(info Installing binary dependencies...)

	pip install grpcio-tools

.protoc-generate:
	$(info Generating proto...)

	python -m grpc_tools.protoc \
	-Icmd/protos \
	--python_out=cmd \
	--pyi_out=cmd \
	--grpc_python_out=cmd \
	cmd/protos/detection.proto

generate: .bin-deps .protoc-generate

.PHONY: \
	.bin-deps \
	.protoc-generate \
	generate
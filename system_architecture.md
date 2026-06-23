# SGIN-HFT System Architecture

## Core Layers
1. **PHY Layer:** Manages SDR interfaces, FSO alignment, and signal modulation.
2. **Network Layer:** Handles TDMA scheduling, BGP route reflection, and UDP transport.
3. **Security Layer:** QKD key rotation, ZTE handoff validation, and encryption shims.
4. **Application Layer:** Trading execution, order book synchronization, and risk gates.

## Data Flow
- **Hot Path:** Market Data -> `ipc_ring_buffer.py` -> `hft_integrated_engine.py` -> Execution.
- **Cold Path:** Market Data -> `market_data_sink.py` -> Disk (Feather format).
- **Control Path:** `sgin_main_orchestrator.py` manages lifecycle events and hardware watchdogs.

## Communication Protocols
- Inter-process: Shared Memory (POSIX).
- Inter-node: UDP/Custom Binary Frames (via `packet_framer.py`).
- Management: gRPC / REST API (via `sgin_api_gateway.py`).
- 

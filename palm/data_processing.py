# palm/data_processing.py
# 데이터 처리 후 전달과 관련된 파이썬 스크립트
# AP3 - 1 Server -> GCG
class DataProcessingAP3_1:
    # FrameHeader Protocol 생성
    def __init__(self, Version, IPType, FrameType, SecurityEnable, Reserved, SequenceNumber, TransmitterIP, TransmitterPort, PayloadLength):
        self.Version = hex(Version)[2:].rjust(2, '0')
        self.IPType = hex(IPType)[2:].rjust(1, '0')
        self.FrameType = '0'
        self.SecurityEnable = hex(SecurityEnable)[2:].rjust(1, '0')
        self.Reserved = Reserved # 이부분 한번 물어보자 Frame에 포함된것인지
        self.SequenceNumber = hex(SequenceNumber)[2:].rjust(4, '0')
        self.TransmitterIP = TransmitterIP # ip4 일때 ip6일때 다르게 동작
        if self.IPType == '0':
            IPv4 = ''
            for num in self.TransmitterIP.split('.'):
                IPv4 += hex(int(num))[2:].rjust(2,'0')
            self.TransmitterIP = IPv4.rjust(32, '0')
        elif self.IPType == '1':
            IPv6 = ''
            IPv6_string = "".join(self.TransmitterIP.split(':'))
            IPv6_lower = []
            for i in IPv6_string:
                if i.isupper():
                    IPv6_lower.append(i.lower())
                else:
                    IPv6_lower.append(i)
                IPv6 = "".join(IPv6_lower)
            self.TransmitterIP = IPv6
        # IP 저장
        self.TransmitterPort = hex(TransmitterPort)[2:].rjust(4, '0')
        self.PayloadLength = hex(PayloadLength)[2:].rjust(4, '0')
        self.RequestCommand = ''
        self.Payload = ''
        # 생성자 정의

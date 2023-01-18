import { IClienteFormData, IPedido, IVeiculo } from "../interfaces"
import { api, cepApi } from "../services/api"
import { } from 'react-query'
import { useQuery } from "react-query/types/react"

// GET com ou sem Slash
// POST APENAS COM SLASH

export const useApi = () => ({
    signin: async (email: string, password: string) => {
        const response = await api.post('/auth/login/', { email, password })
        return response.data
    },
    logout: async () => {
        const response = await api.get('/auth/logout/', {
            headers: {
                "Authorization": `Token ${localStorage.getItem("authToken")}`
            }
        })
        return response.data
    },
    registerCliente: async ({ full_name, email, cpf, password }: IClienteFormData) => {
        const response = await api.post('/auth/register_cliente/', { full_name, cpf, email, password })
        return response.data
    },
    registerFreteiro: async (data: FormData) => {
        const response = await api.post('/auth/register_freteiro/', data, {
            headers: {
                'Content-Type': 'multipart/form-data',
            }
        })
        return response
    },
    registerPedido: async (pedido: IPedido) => {
        const response = await api.post('/pedido/', pedido, {
            headers: {
                "Authorization": `Token ${localStorage.getItem("authToken")}`
            }
        })
        return response.data
    },
    registerVeiculo: async (veiculo: IVeiculo) => {
        const response = await api.post('/veiculo/', veiculo, {
            headers: {
                "Authorization": `Token ${localStorage.getItem("authToken")}`
            }
        })
    },
    getVeiculos: async () => {
        const response = await api.get('/veiculo/', {
            headers: {
                "Authorization": `Token ${localStorage.getItem("authToken")}`
            }
        })
        return response.data
    },
    validateToken: async (token: string) => {
        const response = await api.get('/auth/user/', {
            headers: {
                "Authorization": `Token ${token}`
            }
        })
        return response.data
    },
    tiposVeiculo: async () => {
        const response = await api.get('/tipodeveiculo/', {
            headers: {
                "Authorization": `Token ${localStorage.getItem("authToken")}`
            }
        })
        return response.data
    },
    getPedidos: async () => {
        const response = await api.get('/pedido/', {
            headers: {
                "Authorization": `Token ${localStorage.getItem("authToken")}`
            }
        })
        return response.data
    },
    getSearchPedidos: async (queryString: any) => {
        const response = await api.get(`/pedido/?${queryString}`, {
            headers: {
                "Authorization": `Token ${localStorage.getItem("authToken")}`
            }
        })
        return response.data
    },
    getPedido: async (id: number) => {
        const response = await api.get(`/pedido/${id}`, {
            headers: {
                "Authorization": `Token ${localStorage.getItem("authToken")}`
            }
        })
        return response.data
    },
    getCliente: async (id: number | undefined) => {
        const response = await api.get(`/cliente/${id}/`, {
            headers: {
                "Authorization": `Token ${localStorage.getItem("authToken")}`
            }
        })
        return response.data
    },
    getFreteiro: async (id: number | undefined) => {
        const response = await api.get(`/freteiro/${id}/`, {
            headers: {
                "Authorization": `Token ${localStorage.getItem("authToken")}`
            }
        })
        return response.data
    },
    getUser: async () => {
        const response = await api.get(`/auth/user/`, {
            headers: {
                "Authorization": `Token ${localStorage.getItem("authToken")}`
            }
        })
        return response.data
    },
    getTypeUser: async (id: number) => {
        const response = await api.get(`usuarios/${id}/`, {
            headers: {
                "Authorization": `Token ${localStorage.getItem("authToken")}`
            }
        })
        return response.data
    },
    updateFreteiro: async (id: number, data: FormData) => {
        const response = await api.patch(`/freteiro/${id}/`, data, {
            headers: {
                "Authorization": `Token ${localStorage.getItem("authToken")}`,
                'Content-Type': 'multipart/form-data',
            }
        })
        return response.data
    },
    updateCliente: async (id: number, data: FormData) => {
        const response = await api.patch(`/cliente/${id}/`, data, {
            headers: {
                "Authorization": `Token ${localStorage.getItem("authToken")}`,
                'Content-Type': 'multipart/form-data',
            }
        })
        return response.data
    },
    getCEP: async (cep: string) => {
        const response = await cepApi.get(`/${cep}/json/`)
        return response.data
    }
})

export default useApi